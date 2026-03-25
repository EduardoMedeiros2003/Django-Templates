from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
from django.db.models import Q

def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicado=True)

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicado=True)# Pega todos os itens do banco de dados

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']# referencia ao buscar do buscar.html / pega o nome da busca 
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)#vai procurar se o nome faz sentido no projeto

    # Vai fazer a busca pela legenda 
    fotografias = Fotografia.objects.filter(
    Q(nome__icontains=nome_a_buscar) |
    Q(legenda__icontains=nome_a_buscar),
    publicado=True
)

    return render(request, 'galeria/buscar.html', {"cards": fotografias})

