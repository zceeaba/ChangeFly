from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Signin, name='Signin'),
    url(r'^Signup/', views.Signup, name='Signup'),
    url(r'^transaction/', views.transactionpage, name='Transactions'),
]
