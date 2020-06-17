from django.shortcuts import render
from .models import *


def base(request):
    return render(request, 'baseConhecimento/base.html')
