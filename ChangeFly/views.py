# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

from django.http import  HttpResponse
from django.shortcuts import render
from .forms import NewUserForm
from django.core.urlresolvers import reverse
from .models import Users
from django.http import HttpResponseRedirect
from tables import customer_infoTable
from ChangeFly.models import customer_info

# Create your views here.
from ChangeFly.forms import LoginForm,ImportExcelForm
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from django.template import Template,Context



def login(request):
    username = "not logged in"

    if request.method == "POST":
        # Get the posted form
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            password = MyLoginForm.cleaned_data['password']
            if MyLoginForm.clean_message():
                return HttpResponseRedirect('transactions/')
                #return HttpResponseRedirect('/transactions')
                #return render(request, 'loggedin.html', {"username": username})
            else:
                return HttpResponse("User not found")

    else:
        MyLoginForm = LoginForm()

def trans(request):
    return render(request, 'transaction.html')



def Signin(request):
    return HttpResponse("This is the sign in page")

def Signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            emailaddress=form.cleaned_data.get('EmailAddress')
            user = Users(username=username, password=password,EmailAddress=emailaddress)
            return HttpResponse("Congrats on signing up")
    else:
        form = NewUserForm()
    return render(request, 'SignUp.html', {'form': form})

from .models import customer_info
from django.views import generic
# Create your views here.

class transactionView(generic.ListView):
    model = customer_info
    context_object_name = 'object_list'  # your own name for the list as a template variable
    template_name = 'transaction.html'

    def get_queryset(self):
        return customer_info.objects.all()

from django.db import connection
import sqlite3
import sys

def _my_custom_sqlitedatabase():
    try:
        con = sqlite3.connect('C:/Users/baans/PycharmProjects/ChangeFly/customer_info.db')

        cursor = con.cursor()

        cursor.execute('SELECT * FROM roundups')

        data = cursor.fetchall()

        for record in data:
            print record

        return data
    except sqlite3.Error as e:

        if con:
            con.rollback()

        print("Error %s:" % e.args[0])
        sys.exit(1)

    finally:
        if con:
            con.close()


from django.http import HttpResponse
from django.template import loader

"""
def rendertemplate(request,record):
    template = loader.get_template('customerlist.html')
    context = {"record":{"Company name": record[0], "Amount": record[1], "Rounded up": record[2], "Donation": record[3],
         "randomdata": record[4], "Date": record[5],
         "ID": record[6]}}
    return render(request, template, context)

    
    table = customer_infoTable(customer_info.objects.all())

    return render(request, 'customerlist.html', {
        'table': table
    })
    """
"""
def customer_list(request):
    data = _my_custom_sqlitedatabase()
    for record in data:
        rendertemplate(request,record)
"""
"""
from django.core.mail import send_mail
from django.http import HttpResponse

def sendSimpleEmail(request,emailto):
   res = send_mail("hello Jay", "comment tu vas?", "zceeaba@ucl.ac.uk", ["abhishekhb@yahoo.co.uk"])
   return HttpResponse('%s'%res)

from django.http import HttpResponse
from django.template import loader
"""

