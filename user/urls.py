from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'listar_usuario/$', listar_usuario, name='listar_usuario'),
    url(r'logar/$', logar, name='logar'),
    url(r'deslogar/$', deslogar, name='deslogar'),
]