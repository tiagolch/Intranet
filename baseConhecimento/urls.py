from django.urls import path

from baseConhecimento import views

urlpatterns = [
    path('', views.base, name='base'),
]