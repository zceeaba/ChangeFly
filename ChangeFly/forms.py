from django import forms
from ChangeFly.models import Users


class NewUserForm(forms.ModelForm):
    """
    username = forms.CharField(label='username', max_length=100, help_text="Please enter the username.")
    EmailAddress = forms.CharField(label='Email Address', max_length=100)
    password = forms.CharField(label='password', max_length=100)
    """

    class Meta:
        model = Users
        fields = ['username','EmailAddress','password',]



