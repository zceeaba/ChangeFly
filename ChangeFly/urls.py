from django.conf.urls import url

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.Signin, name='Signin'),
    url(r'^Signup/', views.Signup, name='Signup'),
    url(r'^transaction/', views.transactionpage, name='Transactions'),
    url(r'^login/', views.login, name='login'),
    url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
]
