# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render

# Create your views here.
def Signin(request):
    return HttpResponse("This is the sign in page")

def Signup(request):
    return render(request,'SignUp.html')

def transactionpage(request):
    return render(request,'transaction.html')