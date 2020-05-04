from django.shortcuts import render
from .models import Notificacao, Categoria

def notificacao(request):
    notificacao = Notificacao.objects.filter(ativo=True).order_by('data_criacao').reverse()
    dados = {
        'notificacao': notificacao
    }
    return render(request, 'notificacao/notificacao.html', dados)