from django.contrib import admin
from .models import *

@admin.register(Cotacao_Frete)
class Cotacao_Frete_Admin(admin.ModelAdmin):
    list_display = ['empresa','data', 'pedido', 'nota_fiscal', 'nome_cliente', 'cidade', 'uf', 'quantidade', 'peso', 'cubagem', 'valor', 'frete']
    list_filter = ['empresa']
    search_fields = ['nome_cliente']


@admin.register(Tipo_Frete)
class Tipo_Frete_Admin(admin.ModelAdmin):
    list_display = ['frete']
    search_fields = ['frete']


@admin.register(Cliente)
class Cliente_Admin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']



