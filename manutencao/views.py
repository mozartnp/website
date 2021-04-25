from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from .models import TextoEmpresa

def manutencao(request):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:
        return render(request, 'manutencao.html')
    else:
        return redirect('login')

def dados(request):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:
        return render(request, 'manutencao_templates/dadosempresa.html')
    else:
        return redirect('login')

def sobre(request):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        sobre_nos = TextoEmpresa.objects.all()

        dados = {
            'sobre_nos' : sobre_nos
        }
        
        return render(request, 'manutencao_templates/sobrenos.html',  dados)
    else:
        return redirect('login')

def categoria(request):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:
        return render(request, 'manutencao_templates/categoria.html')
    else:
        return redirect('login')

def produto(request):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:
        return render(request, 'manutencao_templates/produto.html')
    else:
        return redirect('login')

