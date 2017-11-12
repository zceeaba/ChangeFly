from django import forms
from ChangeFly.models import Users



class NewUserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['username','EmailAddress','password',]


class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(max_length = 100)

   def clean_message(self):
       username = self.cleaned_data.get("username")
       password = self.cleaned_data.get("password")
       dbuser = Users.objects.filter(username=username,password=password)

       if not dbuser:
           return None
       else:
        return username

class ImportExcelForm(forms.Form):
    file  = forms.FileField(label= "Choose excel to upload")



