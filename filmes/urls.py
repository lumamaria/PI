from django.urls import path, include
from . import views

app_name = 'filmes'

urlpatterns = [
    path('lista/', views.lista, name='lista'),
    path('detalhe/', views.detalhe, name='detalhe'),
]