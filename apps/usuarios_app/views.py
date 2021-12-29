from django.shortcuts import get_object_or_404, redirect, render

from produtos_app.models import *
from .models import *

from django.contrib import auth, messages
from django.contrib.auth.models import User

def cadastro_usuario(requisicao):
    if requisicao.method == 'POST':
        nome = requisicao.POST['nome']
        email = requisicao.POST['email']
        senha = requisicao.POST['senha']
        senha_confirmacao = requisicao.POST['senha_confirmacao']

        # Validar campos
        # Verificar se o usuario já existe
        if User.objects.filter(email=email).exists():
            messages.error(requisicao, 'Usuario já cadastrado')
            return redirect('cadastro_usuario')
        if campo_vazio(nome):
            messages.error(requisicao, 'O campo nome não pode ficar em branco')
            return redirect('cadastro_usuario')
        if campo_vazio(email):
            messages.error(requisicao, 'O campo email não pode ficar em branco')
            return redirect('cadastro_usuario')
        if campo_vazio(senha):
            messages.error(requisicao, 'O campo senha não pode ficar em branco')
            return redirect('cadastro_usuario')
        if campo_vazio(senha_confirmacao):
            messages.error(requisicao, 'O campo de confirmação de senha não pode ficar em branco')
            return redirect('cadastro_usuario')
        if senha != senha_confirmacao:
            messages.error(requisicao, 'Senhas não conferem')
            return redirect('cadastro_usuario')

        # Inserir usuario no banco
        usuario = User.objects.create_user(username=nome,email=email, password=senha)
        usuario.save()
        messages.success(requisicao, 'Usuario criado com sucesso')
        return redirect('login')
        
    return render(requisicao, 'usuarios/cadastro_usuario.html')

def login(requisicao):
    if requisicao.method == 'POST':
        email = requisicao.POST['email']
        senha = requisicao.POST['senha']
        if not email.strip() or not senha.strip():
            messages.error(requisicao, 'Os campos não podem ficar em branco')
            return redirect('login')
        
        if User.objects.filter(email=email).exists:
            nome = nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            usuario = auth.authenticate(requisicao, username=nome, password=senha)
            if usuario is not None:
                auth.login(requisicao, usuario)
                messages.success(requisicao, 'Login realizado com sucesso')
                #Redirecionar para catalogo de produtos cadastrados, com opção de edição e adição de novos produtos
                return redirect('produtos')
    
    return render(requisicao, 'usuarios/login.html')


def logout(requisicao):
    auth.logout(requisicao)
    return redirect('pagina_inicial')
  

def campo_vazio(campo):
    return not campo.strip()



