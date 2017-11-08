"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'app.views.pagina_inicial', name='pagina_inicial'),
    url(r'^contato$', 'app.views.contato', name='contato'),
    url(r'^desenvolvido', 'app.views.desenvolvido', name='desenvolvido'),

    url(r'^cadastro_alunos', 'app.views.cadastro_alunos', name='cadastro_alunos'),
    url(r'^novo_aluno', 'app.views.novo_aluno', name='novo_aluno'),

    url(r'^cadastro_candidatos', 'app.views.cadastro_candidatos', name='cadastro_candidatos'),
    url(r'^novo_candidato', 'app.views.novo_candidato', name='novo_candidato'),

    url(r'^cadastro_colaborador', 'app.views.cadastro_colaborador', name='cadastro_colaborador'),
    url(r'^novo_colaborador', 'app.views.novo_colaborador', name='novo_colaborador'),

    url(r'^cadastro_cursos', 'app.views.cadastro_cursos', name='cadastro_cursos'),
    url(r'^novo_curso', 'app.views.novo_curso', name='novo_curso'),

    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

)
