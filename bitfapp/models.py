from django.db import models
from cloudinary.models import CloudinaryField
import datetime

# Create your models here.
class Member(models.Model):
    email = models.EmailField(primary_key=True, max_length=200)
    fname = models.CharField(max_length=200, null=True, blank=True)
    cur = models.CharField(max_length=200, null=True, blank=True, default="€" )
    lname = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    passport = CloudinaryField('passport', blank=True)
    code = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True,default='open')

    ref = models.CharField(max_length=200, null=True, blank=True, default=0.00)
    bal = models.FloatField(default=0.0, blank=True, null=True)
    prof = models.FloatField(default=0.0, blank=True, null=True)
    ref_b = models.FloatField(default=0.0, blank=True, null=True)

    slip = CloudinaryField('slip', blank=True)
    id_type = models.CharField(max_length=200, null=True, blank=True)
    id_b = CloudinaryField('id_b', blank=True)
    id_f = CloudinaryField('id_f', blank=True)
    verify = models.CharField(max_length=200, null=True, blank=True)
    plan = models.CharField(max_length=200, null=True, blank=True)

    msg_head = models.CharField(max_length=200, null=True, blank=True)
    msg_body = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.fname +' '+ self.lname

class Manage(models.Model):
    site = models.CharField(max_length=200, primary_key=True, default='site')
    wallet_id = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    admin_pin = models.CharField(max_length=200, null=True, blank=True, default='1234')
    coupon_code = models.CharField(max_length=200, null=True, blank=True, default='4321')

    def __str__(self):
        return self.site

class Dhistory(models.Model):
    email = models.CharField(blank=True, null=True, max_length=200)
    amt = models.CharField(blank=True, null=True, max_length=200)
    status = models.CharField(blank=True, null=True, max_length=200)
    date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
    def __str__(self):
        return self.email

class Whistory(models.Model):
    email = models.CharField(blank=True, null=True, max_length=200)
    amt = models.CharField(blank=True, null=True, max_length=200)
    status = models.CharField(blank=True, null=True, max_length=200)
    date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
    type = models.CharField(blank=True, null=True, max_length=200)
    def __str__(self):
        return self.email

class subs(models.Model):
    name= models.CharField(primary_key=True, max_length=200)
    depo = models.CharField(blank=True, null=True, max_length=200)
    withs = models.CharField(blank=True, null=True, max_length=200)
    list = models.CharField(blank=True, null=True, max_length=200, default=0)
    time = models.CharField(blank=True, null=True, max_length=200)
    def __str__(self):
        return self.name