from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.models import Curso

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        error_messages = {
            'first_name': {
                'required': 'first_name'
            }
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'periodo', 'instituicao']
