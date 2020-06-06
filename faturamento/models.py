from django.db import models
from ramais.models import Empresa


class Cliente(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome Cliente')

    def __str__(self):
        return self.nome


class Tipo_Frete(models.Model):
    frete = models.CharField(max_length=20)

    def __str__(self):
        return self.frete


class Transportadora(models.Model):
    transportadora = models.CharField(max_length=50, verbose_name='Transportadora')
    


class Cotacao_Frete(models.Model):
    Choice_UF = [
        ('AC','AC'),
        ('AL','AL'),
        ('AP','AP'),
        ('AM','AM'),
        ('BA','BA'),
        ('CE','CE'),
        ('DF','DF'),
        ('ES','ES'),
        ('GO','GO'),
        ('MA','MA'),
        ('MT','MT'),
        ('MS','MS'),
        ('MG','MG'),
        ('PA','PA'),
        ('PB','PB'),
        ('PR','PR'),
        ('PE','PE'),
        ('PI','PI'),
        ('RJ','RJ'),
        ('RN','RN'),
        ('RS','RS'),
        ('RO','RO'),
        ('RR','RR'),
        ('SC','SC'),
        ('SP','SP'),
        ('SE','SE'),
        ('TO','TO')
    ]
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, verbose_name='Empresa')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    pedido = models.CharField(max_length=7, verbose_name='Pedido', null=True, blank=True)
    nota_fiscal = models.CharField(max_length=7, verbose_name='Nota Fiscal', blank=True, null=True)
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Cliente')
    cidade = models.CharField(max_length=50, blank=True, null=True, verbose_name='Cidade')
    uf = models.CharField(max_length=2, choices=Choice_UF, blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True, verbose_name='Quantidade')
    peso = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    cubagem = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    valor = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    frete = models.ForeignKey(Tipo_Frete, on_delete=models.DO_NOTHING, blank=True, null=True)

    def get_data(self):
        return self.data.strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return str(self.empresa) + ' ' + str(self.nome_cliente) + ' ' + str(self.get_data())

