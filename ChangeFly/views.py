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


def customer_list(request):
    table = customer_infoTable(customer_info.objects.all())

    return render(request, 'customerlist.html', {
        'table': table
    })
