from django.shortcuts import render
from usuarios.forms import LoginForms
# Cada app precisa de um diretorio na em templates

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
# Create your views here.
