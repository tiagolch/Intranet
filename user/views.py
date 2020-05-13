from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def logar(request, template_name="login.html"):
    next = request.GET.get('next', '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect( next )
        else:
            messages.error(request, 'Usuario ou senha incorretos.')
            return HttpResponseRedirect(settings.LOGIN_URL)
    return  render(request, template_name, {'redirect_to': next})

def deslogar(request):
    logout(request)
    return HttpResponseRedirect( settings.LOGIN_URL )

@login_required
def listar_usuario(request, template_name='listar_usuario.html'):
    usuarios = User.objects.all()
    usuario = {'lista': usuarios}
    return render(request, template_name, usuario)

