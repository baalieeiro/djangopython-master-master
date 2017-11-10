from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Curso
from app.models import Aluno
from app.models import Candidato
from app.models import Colaborador
from datetime import datetime
from app.forms import UserModelForm
from app.forms import CursoForm
from app.forms import AlunoForm
from app.forms import CandidatoForm
from app.forms import ColaboradorForm
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


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

def cadastro(request):
    form = UserModelForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'app/cadastro.html', context)

def novo_curso(request):
    form = CursoForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'app/novo_curso.html', context)

def novo_aluno(request):
    form = AlunoForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'app/novo_aluno.html', context)

def novo_candidato(request):
    form = CandidatoForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'app/novo_candidato.html', context)

def novo_colaborador(request):
    form = ColaboradorForm(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'app/novo_colaborador.html', context)

class apagar_aluno(DeleteView):
    model = Aluno
    success_url = reverse_lazy('cadastro_alunos')

def apagar_aluno(request, pk, template_name='confirmacao_apagar_aluno.html'):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method=='POST':
        aluno.delete()
        return redirect('cadastro_alunos')
    return render(request, template_name, {'object':aluno})

class editar_aluno(UpdateView):
    model = Aluno
    fields = ['ra', 'nome', 'curso', 'data_nascimento', 'email', 'endereco', 'cidade', 'estado', 'telefone', 'celular']
    success_url = reverse_lazy('cadastro_alunos')

def editar_aluno(request, pk, template_name='novo_aluno.html'):
    aluno = get_object_or_404(Aluno, pk = pk)
    form = AlunoForm(request.POST, instance = aluno)
    if form.is_valid():
        form.save()
        return redirect('cadastro_alunos')
    return render(request, template_name, {'form':form})

def apagar_candidato(request, pk, template_name='confirmacao_apagar_candidato.html'):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.method=='POST':
        candidato.delete()
        return redirect('cadastro_candidatos')
    return render(request, template_name, {'object':candidato})
