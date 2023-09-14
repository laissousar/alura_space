from django.shortcuts import render
from django.http import HttpResponse # reponder uma requisição



def index(request): #Função para retornar uma requisição
    dados = {
    1:{"nome": "Nebulosa de Carina",
       "legenda": "webbtelescope.org / NASA / James Webb"},
    2:{"nome": "Galáxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"}
}
    return render(request, 'galeria/index.html', {"cards": dados}) #Passando os dados do dicionario para o index.html
def imagem(request):
    return render(request, 'galeria/imagem.html')