from django.shortcuts import render

# Create your views here.
def lista(request):
    return render(request, 'filmes/lista.html')

def detalhe(request):
    return render(request, 'filmes/detalhe.html')