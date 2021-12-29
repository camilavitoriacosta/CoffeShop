from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import *

def pagina_inicial(requisicao):
    return render(requisicao, 'pagina_inicial.html')

def buscar_produtos_categoria_coffe():
    produtos = filtrar_produto_por_categoria("coffe")    
    dados = {
        'produtos': produtos
    }
    return dados

def catalogo_produtos_coffe(requisicao):
    """ Gera catalogo filtrado pela categoria para usuarios não logados"""  
    return render(requisicao, 'produtos/catalogo_produtos.html', buscar_produtos_categoria_coffe())

def produtos_coffe(requisicao):   
    """ Gera catalogo filtrado pela categoria para usuarios logados"""  
    return render(requisicao, 'usuarios/produtos.html', buscar_produtos_categoria_coffe())

def buscar_produtos_categoria_tea():
    produtos = filtrar_produto_por_categoria("tea")    
    dados = {
        'produtos': produtos
    }
    return dados

def catalogo_produtos_tea(requisicao):  
    """ Gera catalogo filtrado pela categoria para usuarios não logados"""   
    return render(requisicao, 'produtos/catalogo_produtos.html', buscar_produtos_categoria_tea())

def produtos_tea(requisicao):  
    """ Gera catalogo filtrado pela categoria para usuarios logados"""   
    return render(requisicao, 'usuarios/produtos.html', buscar_produtos_categoria_tea())

def buscar_produtos_categoria_smoothie():
    produtos = filtrar_produto_por_categoria("smoothie")    
    return  { 'produtos': produtos }

def catalogo_produtos_smoothie(requisicao):
    """ Gera catalogo filtrado pela categoria para usuarios não logados"""   
    return render(requisicao, 'produtos/catalogo_produtos.html', buscar_produtos_categoria_smoothie())

def produtos_smoothie(requisicao):
    """ Gera catalogo filtrado pela categoria para usuarios logados"""   
    return render(requisicao, 'usuarios/produtos.html', buscar_produtos_categoria_smoothie())

def filtrar_produto_por_categoria(categoria_produto):
    """ Filtra produtos pela categoria especificada """
    return Produto.objects.filter(categoria=categoria_produto)
    
def buscar_produto(requisicao):
    lista_produtos = Produto.objects.all()

    if 'buscar' in requisicao.GET:
        texto_busca = requisicao.GET['buscar']
        lista_produtos = lista_produtos.filter(nome_produto__icontains=texto_busca)
        dados = {
            'produtos': lista_produtos
        }

    return render(requisicao, 'produtos/catalogo_produtos.html', dados)

def produtos(requisicao):
    """ Gera catalogo para usuarios logados"""   
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
