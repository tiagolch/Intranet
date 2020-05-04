from django.contrib import admin
from .models import Categoria, Notificacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'data_criacao', 'ativo']
    list_editable = ['ativo']

@admin.register(Notificacao)
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ['categoria', 'descricao', 'data_criacao', 'data_prazo','data_concluido', 'ativo']
    list_editable = ['ativo']