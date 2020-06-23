from django.shortcuts import render
from .models import base


def base_conhecimento(request):
    busca = request.GET.get('buscar_base')
    if busca:
        result = base.objects.filter(descricao__icontains=busca, ativo=True)
        dados = {
            'busca_base':result
        }
        return render(request, 'baseConhecimento/base_Conhecimento.html', dados)
    else:
        result = base.objects.all()
        dados = {
            'busca_base':result
        }
        return render(request, 'baseConhecimento/base_Conhecimento.html', dados)
