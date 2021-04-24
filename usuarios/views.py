from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method =='POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']

        #Checagem de segurança para usuário e senha.
        user = auth.authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth.login(request, user)
            return redirect('manutencao')
        else:
            print('Usuário ou senha está errado.')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def manutencao(request):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:
        return render(request, 'manutencao.html')
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('index')
