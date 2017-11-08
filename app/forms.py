from django import forms
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

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=200, label=("Login: "), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Senha: "))

class CursoForms(forms.Form):
    nome = forms.CharField(max_length=100, label=("Nome: "), error_messages={'required': 'Nome'})
    periodo = forms.CharField(max_length=50, label=("Periodo: "), error_messages={'required': 'Periodo'})
    instituicao = forms.CharField(max_length=200, label=("Instituição: "), error_messages={'required': 'Instituição'})

class AlunoForms(forms.Form):
    nome = forms.CharField(max_length=200, label=("Nome: "), error_messages={'required': 'Nome'})
    ra = forms.CharField(max_length=10, label=("Ra: "), error_messages={'required': 'Ra'})
    curso = forms.CharField(max_length=100, label=("Curso: "), error_messages={'required': 'Curso'})
    data_nascimento = forms.CharField(max_length=15, label=("Data de nascimento: "), error_messages={'required': 'Data de nascimento'})
    email = forms.CharField(max_length=100, label=("Email: "), error_messages={'required': 'Email'})
    endereco = forms.CharField(max_length=200, label=("Endereço: "), error_messages={'required': 'Endereço'})
    cidade = forms.CharField(max_length=100, label=("Cidade: "), error_messages={'required': 'Cidade'})
    estado = forms.CharField(max_length=10, label=("Estado: "), error_messages={'required': 'Estado'})
    telefone = forms.CharField(max_length=15, label=("Telefone: "), error_messages={'required': 'Telefone'})
    celular = forms.CharField(max_length=15, label=("Celular: "), error_messages={'required': 'Celular'})

class CandidatoForms(forms.Form):
    nome = forms.CharField(max_length=200, label=("Nome: "), error_messages={'required': 'Nome'})
    curso = forms.CharField(max_length=100, label=("Curso: "), error_messages={'required': 'Curso'})
    data_nascimento = forms.CharField(max_length=15, label=("Data de nascimento: "), error_messages={'required': 'Data de nascimento'})
    email = forms.CharField(max_length=100, label=("Email: "), error_messages={'required': 'Email'})
    endereco = forms.CharField(max_length=200, label=("Endereço: "), error_messages={'required': 'Endereço'})
    cidade = forms.CharField(max_length=100, label=("Cidade: "), error_messages={'required': 'Cidade'})
    estado = forms.CharField(max_length=10, label=("Estado: "), error_messages={'required': 'Estado'})
    telefone = forms.CharField(max_length=15, label=("Telefone: "), error_messages={'required': 'Telefone'})
    celular = forms.CharField(max_length=15, label=("Celular: "), error_messages={'required': 'Celular'})

class ColaboradorForms(forms.Form):
    nome = forms.CharField(max_length=200, label=("Nome: "), error_messages={'required': 'Nome'})
    cargo = forms.CharField(max_length=100, label=("Cargo: "), error_messages={'required': 'Cargo'})
    data_nascimento = forms.CharField(max_length=15, label=("Data de nascimento: "), error_messages={'required': 'Data de nascimento'})
    email = forms.CharField(max_length=100, label=("Email: "), error_messages={'required': 'Email'})
    endereco = forms.CharField(max_length=200, label=("Endereço: "), error_messages={'required': 'Endereço'})
    cidade = forms.CharField(max_length=100, label=("Cidade: "), error_messages={'required': 'Cidade'})
    estado = forms.CharField(max_length=10, label=("Estado: "), error_messages={'required': 'Estado'})
    telefone = forms.CharField(max_length=15, label=("Telefone: "), error_messages={'required': 'Telefone'})
    celular = forms.CharField(max_length=15, label=("Celular: "), error_messages={'required': 'Celular'})
