from django.conf.urls import urls
from . import views

urlpatterns = [
    url(r'^cadastro$', views.cadastro, name='cadastro')
]
