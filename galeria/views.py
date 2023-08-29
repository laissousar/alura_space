from django.shortcuts import render
from django.http import HttpResponse # reponder uma requisição

def index(request): #Função para retornar uma requisição
    return render(request, 'galeria/index.html')
def imagem(request):
    return render(request, 'galeria/imagem.html')