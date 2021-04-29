from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
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

def editacategoria(request, id_decategoria):

   

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        if request.method == 'POST':

            novo_nome = request.POST['edicategoria']
            Categoria.objects.filter(id=id_decategoria).update(nome_da_categoria=novo_nome)
            return redirect('categoria')
        
        else:

            categoria = get_object_or_404(Categoria, pk=id_decategoria) 

            categoria_a_exibir = {
                'categoria' : categoria
            }
            
            return render(request, 'manutencao_templates/editacategoria.html', categoria_a_exibir)
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

