from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Signin, name='Signin'),
    url(r'^Signup/', views.Signup, name='Signup'),
    #url(r'^get_user/$', views.get_user, name='get_user'),  # NEW MAPPING!
    url(r'^transaction/', views.transactionpage, name='Transactions'),
]
