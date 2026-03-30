from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms
# Cada app precisa de um diretorio na em templates

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {'form': form})#Dicionario obrigatorio para pegar
# Create your views here.
