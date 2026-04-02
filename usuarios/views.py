from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages
# Cada app precisa de um diretorio na em templates

"""
1 - verificamos se a requisição é do tipo POST (envio do formulário);
2 - validamos os dados utilizando o Django Forms;
3 - capturamos os dados do formulário (nome e senha);
4 - utilizamos o authenticate para verificar se o usuário existe e se a senha está correta;
5 - caso o usuário seja válido, realizamos o login com auth.login;
6 - redirecionamos o usuário para a página inicial após login;
7 - caso falhe, redirecionamos de volta para a tela de login.
"""
def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha,
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar o login!')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

'''
1 - verificamos a validação do formulário;
2 - verificamos se as senhas são iguais;
3 - inserimos as informações recebidas no formulário nas variáveis nome, email e senha, para tornar esses dados mais maleáveis na lógica;
4 - verificamos se a informação de nome corresponde a algo já existente no banco de dados;
5 - criamos esse novo usuário com as informações inseridas no formulário.
'''
def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                messages.error(request, 'Senhas não são iguais')
                return redirect ('cadastro')

            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request,'Usuário cadastrado com sucesso')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})