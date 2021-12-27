from django.shortcuts import redirect, render

# Create your views here.
def cadastro_usuario(requisicao):
    if requisicao.method == 'POST':
        print('Usuario criado com sucesso')
        return redirect('login')

    return render(requisicao, 'usuarios/cadastro_usuario.html')

def login(requisicao):
    return render(requisicao, 'usuarios/login.html')

def logout(requisicao):
    pass