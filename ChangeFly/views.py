# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

from django.http import  HttpResponse
from django.shortcuts import render
from .forms import NewUserForm
from django.core.urlresolvers import reverse
from .models import Users
from django.http import HttpResponseRedirect


# Create your views here.
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
            return HttpResponseRedirect(reverse(transactionpage))
    else:
        form = NewUserForm()
    return render(request, 'SignUp.html', {'form': form})

def transactionpage(request):
    return render(request,'transaction.html')


