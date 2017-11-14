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

from django.db import connection
import sqlite3
import sys


class customer_info(models.Model):
    storename=models.CharField(max_length=150)
    amount = models.FloatField(max_length=150)
    rounded_amount = models.IntegerField()
    donation = models.FloatField(max_length=150)
    date = models.CharField(max_length=150)
    transactionid= models.IntegerField()

def _my_custom_sqlitedatabase():
    try:
        con = sqlite3.connect('C:/Users/baans/PycharmProjects/ChangeFly/customer_info.db')

        cursor = con.cursor()

        cursor.execute('SELECT * FROM roundups')

        data = cursor.fetchall()

        for record in data:
            cs=customer_info(storename=(record[0]),amount=float(record[1]),rounded_amount=int(record[2]),donation=float(record[3]),date=record[4],transactionid=int(record[5]))
            cs.save()

        return data
    except sqlite3.Error as e:

        if con:
            con.rollback()

        print("Error %s:" % e.args[0])
        sys.exit(1)

    finally:
        if con:
            con.close()

_my_custom_sqlitedatabase()


"""
class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('Blog.Category')

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
"""
"""
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })
"""