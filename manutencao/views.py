from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

from .models import TextoEmpresa
from produtos.models import Categoria

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

        categorias = Categoria.objects.all()

        dados = {
            'categorias' : categorias
        }

        if request.method == 'POST':
            
            nome_categoria  = request.POST['criarcategoria']
            for x in categorias:
                if nome_categoria == x.nome_da_categoria:
                    messages.error(request, 'Já há um categoria com este nome.')
                    return render(request, 'manutencao_templates/categoria.html', dados)

            messages.success(request, 'Categoria cadastrada com sucesso.')    
            Categoria.objects.create(nome_da_categoria=nome_categoria)
            return redirect('categoria')
            
        return render(request, 'manutencao_templates/categoria.html', dados)
    else:
        return redirect('login')

def produto(request):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        categorias = Categoria.objects.all()

        dados = {
            'categorias' : categorias
        }

        return render(request, 'manutencao_templates/produto.html', dados)
    else:
        return redirect('login')

