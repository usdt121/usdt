from django.shortcuts import render,redirect
from .models import Member,subs, Manage, Dhistory, Whistory
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
import random

# Create your views here.

def home(request):
    site = Manage.objects.get(site='site')

    return render(request, 'index/index.html',{'site':site})

def signup(request):
    if 'email' in request.POST:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        country = request.POST['country']
        phone = request.POST['phone']
        password = request.POST['password']

        request.session['email'] = email
        request.session['name'] = fname +' '+ lname

        new = Member(fname=fname, lname=lname, email=email, country=country, phone=phone
                     , password=password)
        new.save()

        send_mail(
            subject='NEW MEMBER',
            message='A new user just signed in ['+fname+' '+lname+'] '+ ' from ['+ country +']',
            from_email='bit-wiseonlinetrade@bw-support.live',
            recipient_list=['bit-wiseonlinetrade@bw-support.live'],
            fail_silently=True,
        )

        return render(request,'auth/signup2.html')

    if 'passport' in request.POST:
        user = request.session['email']
        update = Member.objects.get(email=user)
        update.passport = request.FILES['img']
        update.save()

        code = random.randrange(1000, 9999)
        request.session['code'] = code
        name = request.session['name']
        print(code)

        html_msg= render_to_string('auth/email_code.html', {'name':name,'code':str(code)},request)
        send_mail(
            subject='BITWISE CODE',
            message='',
            from_email='bit-wiseonlinetrade@bw-support.live',
            recipient_list=[user],
            html_message=html_msg,
            fail_silently=True,
        )

        return render(request, 'auth/signup3.html', {'email':user})
    if 'pin' in request.POST:
        code = request.session['code']
        pin = request.POST['pin']

        if pin == str(code) :
            user = request.session['email']
            update = Member.objects.get(email=user)
            update.code = request.POST['pin']
            update.save()

            return render(request, 'auth/success.html')
            del request.session['code']

        else:
            user = request.session['email']
            return render(request, 'auth/signup3.html', {'email': user,'error':'code not valid'})

    return render(request, 'auth/signup.html')

def login(request):
    if 'user' in request.POST:
        luser = request.POST['user']
        password = request.POST['password']

        try:
            luser = Member.objects.get(email=luser)
            if password == luser.password:
                if luser.code:
                    request.session['luser']=luser.email
                    return redirect('/account/')
                else:
                    cont={'email':luser.email}
                    return render(request, 'auth/signup3.html', cont)
            else:
                cont = {'error':'password not valid'}
                return render(request, 'auth/login.html', cont)

        except ObjectDoesNotExist:
            cont= {'error':'user not found'}
            return render(request, 'auth/login.html', cont)

    return render(request, 'auth/login.html')

# def account(request):
#     if request.session['luser']:
#         luser = request.session['luser']
#         user = Member.objects.get(email=luser)
#         site = Manage.objects.get(site='site')
#         cont = {'user':user,'site':site}
#         return render(request, 'user/account.html', cont)



def acc(request):
    if request.session['luser']:
        user = Member.objects.get(email= request.session['luser'])
        cont ={"user":user}
        return render(request, "users/account.html", cont)

def verify(request):
    if request.session['luser']:
        user = Member.objects.get(email= request.session['luser'])
        cont ={"user":user}
        if "id_type" in request.POST:
            user.id_type = request.POST['id_type']
            user.id_f = request.FILES['id_f']
            user.id_b = request.FILES['id_b']
            user.save()

        return render(request, "users/verify.html", cont)

def profile(request):
    if request.session['luser']:
        user = Member.objects.get(email= request.session['luser'])
        cont ={"user":user}
        if 'pp' in request.POST:
            user.passport = request.FILES['foto']
            user.save()
        if 'update' in request.POST:
            user.fname = request.POST['fname']
            user.lname = request.POST['lname']
            user.email = request.POST['email']
            user.phone = request.POST['phone']
            user.country = request.POST['country']
            user.save()

        if 'pword' in request.POST:
            if request.POST['pword'] == request.POST['pword_c']:
                user.password = request.POST['pword']
                user.save()
            else:
                cont = {"user":user, "info":"Password Does Not Match Try Again"}
                return render(request, "users/profile.html", cont)

        return render(request, "users/profile.html", cont)

def depo(request):
    if request.session['luser']:
        user = Member.objects.get(email= request.session['luser'])
        dhis = Dhistory.objects.filter(email=user.email)
        site =Manage.objects.get(site='site')
        cont ={"user":user}
        if 'amt' in request.POST:
            amt = request.POST['amt']
            new = Dhistory(email=user.email, amt=amt, status="processing..")
            new.save()
            cont = {"user": user,'amt':amt,"Dhis":dhis,'site':site}
            return render(request, "users/wallet.html",cont)
        if 'upload' in request.POST:
            user.slip = request.FILES['slip']
            user.save()
            cont = {"user": user,'info':"info","Dhis":dhis}

            return render(request, "users/wallet.html",cont)

        return render(request, "users/deposit.html",cont)

def act(request):
    if request.session['luser']:
        user = Member.objects.get(email= request.session['luser'])
        try:
            sub =subs.objects.filter(name=user.plan)
            cont = {"user": user,'Sub':sub }
            return render(request, "users/act.html", cont)

        except ObjectDoesNotExist:
            print('hello')
        cont ={"user":user,}
        return render(request, "users/act.html",cont)


def withd(request):
    if request.session['luser']:
        user = Member.objects.get(email= request.session['luser'])
        whis = Whistory.objects.filter(email=user.email)
        cont ={"user":user,'Whis':whis}
        if 'bank' in request.POST:
            bank = request.POST["bank"]
            acc_name = request.POST["acc_name"]
            acc_num = request.POST["acc_num"]
            amt = request.POST["amt"]

            if float(user.bal) < float(amt):
                cont = {"user": user, 'Whis': whis,'error':"INSUFFICIENT FUNDS"}
                return render(request, "users/withdraw.html",cont)

            new = Whistory(email=user.email, type=bank, status='processing..', amt=amt)
            new.save()

            send_mail(
                subject='BANK WITHDRAW REQUEST BY'+'['+ user.fname+' '+user.lname+']',
                message='['+ user.fname+' '+user.lname+'] is requesting a withdraw of : '+user.cur+amt+'To BANK ='+bank+' Accoun_name='+acc_name+' Account-num='+acc_num,
                from_email='exocoins@exocoin.us',
                recipient_list=['exocoin.trade@gmail.com'],
                fail_silently=True
            )

            return render(request, "users/suc.html", cont)

        if 'wallet' in request.POST:
            wallet = request.POST["wallet"]
            coin = request.POST["coin"]
            amt = request.POST["amt"]

            if float(user.bal) < float(amt):
                cont = {"user": user, 'Whis': whis,'error':"INSUFFICIENT FUNDS!!!!"}
                return render(request, "users/withdraw.html",cont)


            new = Whistory(email=user.email, type=wallet, status='processing..', amt=amt)
            new.save()

            send_mail(
                subject='WALLET TRANSFER REQUEST BY'+'['+ user.fname+' '+user.lname+']',
                message='['+ user.fname+' '+user.lname+'] is requesting a withdraw of : '+user.cur+amt+'To WALLET ADDRESS ='+wallet+' Coin='+coin,
                from_email='exocoins@exocoin.us',
                recipient_list=['exocoin.trade@gmail.com'],
                fail_silently=True
            )
            return render(request, "users/suc.html", cont)

        return render(request, "users/withdraw.html",cont)

def plan(request):
    if request.session['luser']:
        site = Manage.objects.get(site="site")
        user = Member.objects.get(email= request.session['luser'])
        sub = subs.objects.all()
        if 'sub' in request.POST:
            amt = request.POST['amt']
            name = request.POST['sub']
            try:
                sub = subs.objects.get(name=name)
                if int(user.bal) > int(sub.list):
                    user.plan=name
                    return redirect('/act/')
                else:
                    cont = {"site": site, 'Sub': sub, 'user': user,"error": "BALANACE IS TOO LOW"}
                    return render(request, "users/plan.html", cont)

            except ObjectDoesNotExist:
                cont = {"site": site, 'Sub': sub, 'user': user}

        cont={"site":site,'Sub':sub,'user':user}

        return render(request, "users/plan.html", cont)

def ref(request):
    return render(request, "users/ref.html")

def livetrade(request):
    return render(request, "users/livetrade.html")

def admin(request):
    if request.session['luser']:
        users = Member.objects.all().order_by('fname')
        cont={"User":users}
        if request.GET.get('del'):
            del_user = Member.objects.get(email=request.Get.get('del'))
            del_user.delete()
        return render(request, "admins/admin.html",cont)

def edit(request):
    if request.session['luser']:
        users = Member.objects.get(email=request.GET.get('edit'))
        dhis = Dhistory.objects.filter(email=users.email)
        whis = Whistory.objects.filter(email=users.email)

        cont={"user":users,'Dhis':dhis}

        if 'body' in request.POST:
            users.msg_head = request.POST['head']
            users.msg_body = request.POST['body']
            users.save()

        if 'apps' in request.POST:
            apps = request.POST['apps']
            apps_dhis = Whistory.objects.get(pk=apps)
            apps_dhis.status="Approved"
            apps_dhis.save()

        if 'deles' in request.POST:
            deles = request.POST['deles']
            deles_dhis = Whistory.objects.get(pk=deles)
            deles_dhis.delete()

        if 'app' in request.POST:
            app = request.POST['app']
            app_dhis = Dhistory.objects.get(pk=app)
            app_dhis.status="Approved"
            app_dhis.save()

        if 'dele' in request.POST:
            dele = request.POST['dele']
            dele_dhis = Dhistory.objects.get(pk=dele)
            dele_dhis.delete()

        if 'addup' in request.POST:
            add = request.POST['addup']
            users.bal= float(users.bal)+float(add)
            users.prof = float(users.prof)+float(add)
            users.save()

        if 'bal' in request.POST:
            users.bal = request.POST['bal']
            users.prof = request.POST['prof']
            users.ref_b = request.POST['ref_b']
            users.cur = request.POST['cur']
            users.save()

        if 'verify' in request.POST:
            users.verify="verified"
            users.save()

        if request.GET.get('edit'):
            users = Member.objects.get(email=request.GET.get('edit'))
            cont = {"user": users, 'Dhis': dhis,'Whis':whis}
        return render(request, "admins/edits.html",cont)

def site(request):
    if request.session['luser']:
        site = Manage.objects.get(site="site")
        sub = subs.objects.all()
        cont={"site":site,'Sub':sub}
        if 'wallet' in request.POST:
            site.wallet_id = request.POST['wallet']
            site.save()
        if 'sub' in request.POST:
            name= request.POST['sub']
            depo = request.POST['depo']
            withs = request.POST['withs']
            time = request.POST['time']
            list = request.POST['list']
            new = subs(name=name, depo=depo,withs=withs,time=time,list=list)
            new.save()

        if request.GET.get('del'):
            del_sub = subs.objects.get(name=request.GET.get('del'))
            del_sub.delete()

        return render(request,'admins/site.html',cont)
