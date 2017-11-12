# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
"""
class Transactions(models.Model):
    accountnumber=models.CharField(max=200)
    sortcode=models.CharField(max=200)
    paymentamount=models.CharField(max=200)
    def __str__(self):
        return self.accountnumber
    def calculatepoints(self):
        newlist=[]
        data=[]
        data.append(self.accountnumber,self.paymentamount)
        newlist.append(data)
        for i in newlist:
"""

class Users(models.Model):
    username=models.CharField(max_length=200)
    EmailAddress=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self):
        return  str(self.username)+str(self.password)

"""
def ProductSelection(request, template_name='product_selection.html'):
    if user.is_authenticated():
        user = request.user
    else:
    # deal with anonymous user info
    user = Users.objects.create(
        user=form.cleaned_data["username"],
        product=form.cleaned_data["product"],
        quantity=form.cleaned_data["product_quantity"],
    )

"""
"""
def getusername(self,username):
    self.username=username
def getname(self,name):
    self.name=name
def getemailid(self,emailid):
    self.EmailAddress=emailid
def getpassword(self,password):
    self.password=password
"""

