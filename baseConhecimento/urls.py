from django.urls import path

from baseConhecimento import views

urlpatterns = [
    path('base', views.base, name='base'),
]