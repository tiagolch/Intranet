from django.contrib import admin
from .models import *

@admin.register(base)
class baseAdmin(admin.ModelAdmin):
    list_display = ['usuario','titulo','data_criacao','data_alteracao','descricao','solucao','imagem','ativo']
    list_editable = ['ativo']
    list_filter = ['categoria', 'ativo', 'usuario']

@admin.register(categoria)
class categoriaAdmin(admin.ModelAdmin):
    list_display = ['nome_categoria','ativo']
    list_editable = ['ativo']