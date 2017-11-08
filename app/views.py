from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Curso
from app.models import Aluno
from app.models import Candidato
from app.models import Colaborador
from datetime import datetime

def pagina_inicial(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Pagina inicial',
            'year':datetime.now().year,
        })
    )

def contato(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contato.html',
        context_instance = RequestContext(request,
        {
            'title':'Contato',
            'message':'Entre em contato conosco',
            'year':datetime.now().year,
        })
    )

def desenvolvido(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/desenvolvido.html',
        context_instance = RequestContext(request,
        {
            'title':'Desenvolvido',
            'message':'Equipe de desenvolvimento',
            'year':datetime.now().year,
        })
    )

def cadastro_alunos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_alunos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de alunos',
            'alunos': Aluno.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_aluno(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/novo_aluno.html',
        context_instance = RequestContext(request,
        {
            'title':'Novo aluno',
            'message':'Novo aluno',
            'year':datetime.now().year,
        })
    )


def cadastro_candidatos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_candidatos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de candidatos',
            'candidatos': Candidato.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_candidato(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/novo_candidato.html',
        context_instance = RequestContext(request,
        {
            'title':'Novo candidato',
            'message':'Novo candidato',
            'year':datetime.now().year,
        })
    )


def cadastro_colaborador(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_colaborador.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de colaborador',
            'colaboradores': Colaborador.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_colaborador(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/novo_colaborador.html',
        context_instance = RequestContext(request,
        {
            'title':'Novo colaborador',
            'message':'Novo colaborador',
            'year':datetime.now().year,
        })
    )


def cadastro_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_cursos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de cursos',
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_curso(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/novo_curso.html',
        context_instance = RequestContext(request,
        {
            'title':'Novo curso',
            'message':'Novo curso',
            'year':datetime.now().year,
        })
    )


def cadastro_usuarios(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_usuarios.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de usuarios',
            'usuarios': Usuario.objects.all(),
            'year':datetime.now().year,
        })
    )

def novo_usuario(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/novo_usuario.html',
        context_instance = RequestContext(request,
        {
            'title':'Novo usuario',
            'message':'Novo usuario',
            'year':datetime.now().year,
        })
    )
