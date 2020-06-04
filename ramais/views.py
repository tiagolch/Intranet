from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Funcionario, Setor


def index(request):
    busca = request.GET.get( 'buscar' )
    if busca:
        result = Funcionario.objects.filter( nome__icontains=busca, ativo=True )
        result1 = {
            'core': result
        }

    if busca:
        result = Setor.objects.filter( setor__icontains=busca )
        result2 = {
            'core': result
        }

    else:

        result = Funcionario.objects.order_by('nome').filter(ativo=True)
        result = {
            'core': result
        }

    return render(request, 'ramais/index.html', result)

