from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from models import Curso
from models import Aluno
from models import Candidato
from models import Colaborador

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

class AlunoForm(forms.ModelForm):
    nome = forms.CharField(
    max_length=30,
    widget=forms.TextInput(
        attrs={
            'style': 'border-color: green;',
            'placeholder': 'Write your name here'
        }
    )
)
    class Meta:
        model = Aluno
        fields = ['nome', 'ra', 'curso', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone', 'celular']

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'curso', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone', 'celular']

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'cargo', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone', 'celular']
