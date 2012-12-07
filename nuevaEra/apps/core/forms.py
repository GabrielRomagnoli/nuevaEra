from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class UserForm(forms.Form):
    
    username = forms.CharField(label=_("Usuario"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password_confirm = forms.CharField(label=_("Confirmar password"), widget=forms.PasswordInput)
    email = forms.EmailField(label=_("Email"), required=True)
