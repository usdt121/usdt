from django.contrib import admin
from . models import Member,subs, Manage, Dhistory, Whistory

# Register your models here.
admin.site.register(Member)
admin.site.register(Manage)
admin.site.register(Dhistory)
admin.site.register(Whistory)
admin.site.register(subs)