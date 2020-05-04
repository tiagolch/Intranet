from django.db import models

# Create your models here.

class Categoria(models.Model):
    descricao = models.CharField(max_length=50, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'categoria'


class Notificacao(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(max_length=300, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now=True,verbose_name='Data do Registro')
    data_prazo = models.DateTimeField(verbose_name='Prazo')
    data_concluido = models.DateTimeField(blank=True, null=True, verbose_name='Conclusão')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.categoria)

    def get_data_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y %H:%M')
    #
    # def get_data_input_prazo(self):
    #     return self.data_prazo.strftime('%Y-%m-%dT%H:%M')

    def get_data_prazo(self):
        return self.data_prazo.strftime( '%d/%m/%Y %H:%M' )

    def get_data_input_conclusao(self):
        return self.data_concluido.strftime('%Y-%m-%dT%H:%M')


    class Meta:
        db_table = 'notificacao'


