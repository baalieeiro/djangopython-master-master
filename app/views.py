from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Curso
from app.models import Aluno
from app.models import Candidato
from app.models import Colaborador
from app.models import Usuario
from datetime import datetime
from app.forms import UserModelForm
from app.forms import CursoForm
from app.forms import AlunoForm
from app.forms import CandidatoForm
from app.forms import ColaboradorForm
from app.forms import UsuarioForm
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.forms import ModelForm


def pagina_inicial(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Pagina inicial',
            'year':datetime.now().year,
            'nometeste': 'RodrigoLuiz'
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

def listar_alunos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/listar_alunos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de alunos',
            'alunos': Aluno.objects.all(),
            'year':datetime.now().year,
        })
    )


def listar_candidatos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/listar_candidatos.html',
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


def listar_colaborador(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/listar_colaborador.html',
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


def listar_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/listar_cursos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de cursos',
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )


def listar_usuarios(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/listar_usuarios.html',
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

def cadastro(request):
    form = UserModelForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'app/cadastro.html', context)

def novo_curso(request, template_name='app/novo_curso.html'):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_cursos')
    return render(request, template_name, {'form':form})

def novo_aluno(request, template_name='app/novo_aluno.html'):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, template_name, {'form':form})

def novo_candidato(request, template_name='app/novo_candidato.html'):
    form = CandidatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_candidatos')
    return render(request, template_name, {'form':form})

def novo_colaborador(request, template_name='app/novo_colaborador.html'):
    form = ColaboradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_colaborador')
    return render(request, template_name, {'form':form})

def novo_usuario(request, template_name='app/novo_usuario.html'):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_usuarios')
    return render(request, template_name, {'form':form})

def apagar_usuario(request, pk, template_name='app/confirmacao_apagar_usuario.html'):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method=='POST':
        usuario.delete()
        return redirect('listar_usuario')
    return render(request, template_name, {'object':usuario.nome})


def apagar_aluno(request, pk, template_name='app/confirmacao_apagar_aluno.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('listar_alunos')
    return render(request, template_name, {'object':aluno.nome})

def apagar_candidato(request, pk, template_name='app/confirmacao_apagar_candidato.html'):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.method=='POST':
        candidato.delete()
        return redirect('listar_candidatos')
    return render(request, template_name, {'object':candidato.nome})

def apagar_colaborador(request, pk, template_name='app/confirmacao_apagar_colaborador.html'):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method=='POST':
        colaborador.delete()
        return redirect('listar_colaborador')
    return render(request, template_name, {'object':colaborador.nome})

def apagar_curso(request, pk, template_name='app/confirmacao_apagar_curso.html'):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method=='POST':
        curso.delete()
        return redirect('listar_cursos')
    return render(request, template_name, {'object':curso.nome})


def editar_aluno(request, pk, template_name='app/editar_aluno.html'):
    aluno= get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance = aluno)
    if form.is_valid():
        form.save()
        return redirect('listar_alunos')
    return render(request, template_name, {'form':form})

def editar_usuario(request, pk, template_name='app/novo_usuario.html'):
    usuario= get_object_or_404(Usuario, pk=pk)
    form = UsuarioForm(request.POST or None, instance = usuario)
    if form.is_valid():
        form.save()
        return redirect('lista_usuarios')
    return render(request, template_name, {'form':form})


def editar_candidato(request, pk, template_name='app/novo_candidato.html'):
    if request.user.is_superuser:
        candidato= get_object_or_404(Candidato, pk=pk)
    else:
        candidato= get_object_or_404(Candidato, pk=pk)
    form = CandidatoForm(request.POST or None, instance = candidato)
    if form.is_valid():
        form.save()
        return redirect('listar_candidatos')
    return render(request, template_name, {'form':form})

def editar_colaborador(request, pk, template_name='app/novo_colaborador.html'):
    if request.user.is_superuser:
        colaborador= get_object_or_404(Colaborador, pk=pk)
    else:
        colaborador= get_object_or_404(Colaborador, pk=pk)
    form = ColaboradorForm(request.POST or None, instance = colaborador)
    if form.is_valid():
        form.save()
        return redirect('listar_colaborador')
    return render(request, template_name, {'form':form})

def editar_curso(request, pk, template_name='app/novo_curso.html'):
    if request.user.is_superuser:
        curso = get_object_or_404(Curso, pk=pk)
    else:
        curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance = curso)
    if form.is_valid():
        form.save()
        return redirect('listar_cursos')
    return render(request, template_name, {'form':form})
