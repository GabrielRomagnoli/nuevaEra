from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class UserForm(forms.Form):
    
    username = forms.CharField(label=_("Usuario"), required=True)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput, max_length=20, min_length=5, required=True)
    password2 = forms.CharField(label=_("Confirmar password"), widget=forms.PasswordInput, max_length=20, min_length=5, required=True)
    email = forms.EmailField(label=_("Email"), required=True)
    
    def save(self):
        user = User(
            email = self.cleaned_data["email"],
            username = self.cleaned_data["username"]
        )
        user.set_password(self.cleaned_data["password"])
        user.save()
    
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        #!! check for equal and not none

        if password != password2:
            self._errors["password"]=self.error_class([_(u"Passwords must match.")])
            self._errors["password2"]=self.error_class([_(u"Passwords must match.")])

        return cleaned_data