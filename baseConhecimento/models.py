from django.db import models
from django.contrib.auth.models import User

class categoria(models.Model):
    nome_categoria = models.CharField(max_length=35, verbose_name='Categoria')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return self.nome_categoria

    class Meta:
        db_table = 'categoria_base'


class base(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING,null=True, blank=True )
    titulo = models.CharField(max_length=50, verbose_name='Titulo')
    categoria = models.ManyToManyField(categoria,related_name='base_categoria', verbose_name='Categoria')
    data_criacao = models.DateField(auto_now_add=True, verbose_name='Data Registro')
    data_alteracao = models.DateField(auto_now=True, verbose_name='Ultima Alteração')
    descricao = models.TextField(max_length=1200, verbose_name='Descrição')
    solucao = models.TextField(max_length=1200, null=True, blank=True, verbose_name='Solução')
    imagem = models.ImageField(null=True, blank=True, verbose_name='Imagem')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return self.titulo+' '+str(self.usuario)+' '+str(self.categoria)

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y')

    def get_data_alteracao(self):
        return self.data_alteracao.strftime('%d/%m/%Y')

    class Meta:
        db_table = 'base'



