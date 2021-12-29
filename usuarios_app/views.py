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

### PRODUTOS ###
def produtos(requisicao):
    if requisicao.user.is_authenticated:

        produtos =  Produto.objects.all()
        dados = {
            'produtos': produtos
        }
        
        return render(requisicao, 'usuarios/produtos.html', dados)
    else:
        return redirect('pagina_inicial')


def cadastro_produtos(requisicao):
    if requisicao.method == 'POST':
        inserir_produto(requisicao)
        messages.success(requisicao, 'Produto criado com sucesso')
        return redirect('produtos')
    return render(requisicao, 'produtos/cadastro_produto.html')

def inserir_produto(requisicao):
    nome = requisicao.POST['nome']
    descricao = requisicao.POST['descricao']
    preco = requisicao.POST['preco']
    categoria = requisicao.POST['categoria']
    foto = requisicao.FILES.get('foto-produto', '')

    produto = Produto(nome_produto=nome, descricao=descricao, preco=preco, categoria=categoria, foto_produto=foto)
    produto.save()

def deleta_produto(requisicao, produto_id):
    produto = get_object_or_404(Produto,pk=produto_id)
    produto.delete()
    messages.success(requisicao, 'Produto deletado com sucesso')
    return redirect('produtos')

def edita_produto(requisicao, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    produto_a_editar = { 'produto': produto }
    return render(requisicao, 'produtos/edita_produto.html', produto_a_editar)

def atualizar_produto(requisicao):
    if requisicao.method == 'POST':
        produto_id = requisicao.POST['produto_id']
        produto = Produto.objects.get(pk=produto_id)

        produto.nome = requisicao.POST['nome']
        produto.descricao = requisicao.POST['descricao']
        produto.preco = requisicao.POST['preco']
        produto.categoria = requisicao.POST['categoria']
        produto.foto_produto = requisicao.FILES.get('foto-produto', produto.foto_produto)

        produto.save()

        messages.success(requisicao, 'Produto atualizado com sucesso')
        return redirect('produtos')



