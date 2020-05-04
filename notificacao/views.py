from django.shortcuts import render
from .models import Notificacao, Categoria

def notificacao(request):
    notificacao = Notificacao.objects.order_by('data_criacao').filter(ativo=True)
    dados = {
        'notificacao': notificacao
    }
    return render(request, 'notificacao/notificacao.html', dados)