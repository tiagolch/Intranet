from django.shortcuts import render
from .models import Funcionario

def index(request):
    busca = request.GET.get( 'buscar' )
    if busca:
        result = Funcionario.objects.filter( nome__icontains=busca, ativo=True )
        result = {
            'core': result
        }

    else:

        result = Funcionario.objects.order_by('nome').filter(ativo=True)
        result = {
            'core': result
        }

    return render(request, 'ramais/index.html', result)

