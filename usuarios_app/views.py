from typing import Tuple
from django.shortcuts import redirect, render
from .models import *
from django.contrib import auth

from django.contrib.auth.models import User

# Create your views here.
def cadastro_usuario(requisicao):
    if requisicao.method == 'POST':
        nome = requisicao.POST['nome']
        email = requisicao.POST['email']
        senha = requisicao.POST['senha']
        senha_confirmacao = requisicao.POST['senha_confirmacao']

        # Validar campos
        valida_campos(nome,email,senha,senha_confirmacao)
        #Mostrar mensagem para o usuario de sucesso ou erro
        print('Usuario criado com sucesso')
        return redirect('login')

    return render(requisicao, 'usuarios/cadastro_usuario.html')

def login(requisicao):
    if requisicao.method == 'POST':
        email = requisicao.POST['email']
        senha = requisicao.POST['senha']
        if not email.strip() or not senha.strip():
            print('Os campos não podem ficar em branco')
            return redirect('login')
        
        if User.objects.filter(email=email).exists:
            nome = nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            usuario = auth.authenticate(requisicao, username=nome, password=senha)
            if usuario is not None:
                auth.login(requisicao, usuario)
                print('login realizado com sucesso')
                #Redirecionar para catalogo de produtos cadastrados, com opção de edição e adição de novos produtos
                #return redirect('')
    
    return render(requisicao, 'usuarios/login.html')

def logout(requisicao):
    pass


def valida_campos(nome, email, senha, senha_confirmacao):
    if not email.strip():
        print('O campo email não pode ficar em branco')
        return redirect('cadastro_usuario')
    if not senha.strip():
        print('O campo senha não pode ficar em branco')
        return redirect('cadastro_usuario')
    if not senha_confirmacao.strip():
        print('O campo de confirmação de senha não pode ficar em branco')
        return redirect('cadastro_usuario')
    if senha != senha_confirmacao:
        print('Senhas não conferem')
        return redirect('cadastro_usuario')
    
    # Verificar se o usuario já existe
    if User.objects.filter(email=email).exists():
        print('Usuario já cadastrado')
        return redirect('cadastro_usuario')
    else:
        # Inserir usuario no banco
        cadastrar_Usuario(nome,email, senha)
        return redirect('login')

        

def cadastrar_Usuario(nome, email, senha):
    usuario = User.objects.create_user(username=nome,email=email, password=senha)
    usuario.save()