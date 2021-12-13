from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    ''' Pagina de login do sistema '''
    
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

def logout(request):
    ''' Pagina de logout do sistema '''

    auth.logout(request)
    return redirect('index')
