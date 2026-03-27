from django.shortcuts import render
# Cada app precisa de um diretorio na em templates

def login(request):
    return render(request, 'usuarios/login.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
# Create your views here.
