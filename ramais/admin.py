from django.contrib import admin
from django.contrib.auth import user_logged_in
from ramais.models import Empresa, Setor,Funcionario


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobreNome', 'empresa', 'setor', 'ramal', 'celular', 'skype', 'email', 'ativo']
    list_editable = ['ramal','celular', 'ativo']
    list_filter = ['setor', 'empresa']
    search_fields = ['nome', 'sobreNome', 'ramal']

