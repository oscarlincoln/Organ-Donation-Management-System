from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
        attrs={
            'class':'form-control'
        }
        )
    )
    password = forms.CharField(
        widget= forms.TextInput(
        attrs={
            'class':'form-control'
        }
        )
    )


class SignUpForm(forms.Form):
     username = forms.CharField(
        widget= forms.TextInput(
        attrs={
            'class':'form-control'
        }
        )
    )
     password1 = forms.CharField(
        widget= forms.TextInput(
        attrs={
            'class':'form-control'
        }
        )
    )
     password2 = forms.CharField(
        widget= forms.TextInput(
        attrs={
            'class':'form-control'
        }
        )
    )
     email = forms.CharField(
        widget= forms.TextInput(
        attrs={
            'class':'form-control'
        }
        )
    )
     

     class meta:
          model = User
          fields = ('username','email','password1','password2','is_admin','is_donor_patient','is_doctor')
