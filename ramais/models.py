from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import user_logged_in


class Setor( models.Model ):
    nome = models.CharField( max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.nome


class Empresa( models.Model ):
    nome = models.CharField( max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.nome


class Funcionario( models.Model ):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True )
    nome = models.CharField( max_length=15, blank=False,verbose_name='Nome' )
    sobreNome = models.CharField( max_length=15, blank=False,verbose_name='Sobre Nome' )
    empresa = models.ForeignKey( 'Empresa', on_delete=models.CASCADE )
    setor = models.ForeignKey( 'Setor', on_delete=models.CASCADE )
    ramal = models.CharField( max_length=4, blank=False )
    celular = models.CharField( max_length=9, blank=True )
    skype = models.CharField( max_length=50, blank=True )
    email = models.EmailField(max_length=50, blank=True )
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' ' + self.sobreNome + ' ' + self.ramal + ' ' + str(self.setor)


