from django.conf.urls import url

from . import views
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
    url(r'^$', views.Signin, name='Signin'),
    url(r'^Signup/', views.Signup, name='Signup'),
    #url(r'^login/$', RedirectView.as_view(url=reverse_lazy('transactions')), name='index'),
    #url(r'^transaction/', views.transactionpage, name='Transactions'),
    url(r'^transactions/', views.transactionView.as_view(), name='transactions'),
    #url(r'^login/transaction/$', views.transactionView.as_view(), name='logintransactions'),
    url(r'^login/transactions/', views.trans, name='logintransaction'),
    url(r'^login/', views.login, name='login'),
    url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
    url(r'^customerlist/', TemplateView.as_view(template_name='customerlist.html')),
    #url(r'^simpleemail/(?P<emailto>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/', views.sendSimpleEmail , name = 'sendSimpleEmail'),
]


