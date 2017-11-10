from django.db import models
from django.core.urlresolvers import reverse


class Curso(models.Model):
    nome = models.CharField(max_length=100)#size 25
    periodo = models.CharField(max_length=50)#size 15
    instituicao = models.CharField(max_length=200)#size 25

class Aluno(models.Model):
    ra = models.CharField(max_length=10)#size 10
    nome = models.CharField(max_length=100)#size 35
    curso = models.CharField(max_length=100)#size 25
    data_nascimento = models.CharField(max_length=15)#size 15
    email = models.CharField(max_length=100)#size 35
    endereco = models.CharField(max_length=200)#size 35
    cidade = models.CharField(max_length=100)#size 10
    estado = models.CharField(max_length=10)#size 5
    telefone = models.CharField(max_length=15)#size 10
    celular = models.CharField(max_length=15)#size 10

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('editar_aluno', kwargs={'pk': self.pk})

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=15)
