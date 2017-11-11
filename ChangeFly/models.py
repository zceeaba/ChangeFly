# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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

