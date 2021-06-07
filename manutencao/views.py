import os
import shutil

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.conf import settings

from .models import TextoEmpresa
from produtos.models import Categoria, Iten
from extra import direcionamento_imagem

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

            if Categoria.objects.filter(nome_da_categoria=nome_categoria).exists():
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

        categoria = get_object_or_404(Categoria, pk=id_decategoria) 

        categoria_a_exibir = {
            'categoria' : categoria
        }

        if request.method == 'POST':

            novo_nome = request.POST['edicategoria']
            if Categoria.objects.filter(nome_da_categoria=novo_nome).exists():
                    messages.error(request, 'Já há um categoria com este nome.')
                    return render(request, 'manutencao_templates/editacategoria.html', categoria_a_exibir)
                    
            Categoria.objects.filter(id=id_decategoria).update(nome_da_categoria=novo_nome)
            return redirect('categoria')
        
        else:          
            return render(request, 'manutencao_templates/editacategoria.html', categoria_a_exibir)
    else:
        return redirect('login')

def deletando_categoria(request, id_decategoria):

     #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        categoria = get_object_or_404(Categoria, pk=id_decategoria) 
        deleta = settings.MEDIA_ROOT + '/fotos/' + str(categoria.id)
        if os.path.exists(deleta):
            shutil.rmtree(deleta)
        categoria.delete()
        return redirect('categoria')

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

def editaprodutos(request, id_decategoria):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        categoria = get_object_or_404(Categoria, pk=id_decategoria) 
        produtos = Iten.objects.filter(categoria=categoria)

        dados = {
            'categoria' : categoria ,
            'produtos' : produtos,
        }

        if request.method == 'POST':

            categoria = Categoria.objects.get(id=id_decategoria)
            nomeproduto = request.POST['nomeproduto']
            imagemproduto = request.FILES['imagemproduto']
                        
            Iten.objects.create(categoria=categoria, nome_do_produto=nomeproduto, imagem=imagemproduto)
            direcionamento_imagem.imagem_caminho_produto(nomeproduto)
            
            messages.success(request, 'Produto cadastrado com sucesso.')

            return redirect('editaprodutos', id_decategoria)
              
        return render(request, 'manutencao_templates/editaprodutos.html', dados)
    else:
        return redirect('login')

def editaproduto(request, id_doproduto):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        produto = get_object_or_404(Iten, pk=id_doproduto) 
        
        dados = {
            'produto' : produto
        }  

        if request.method == 'POST':
            item = Iten.objects.get(id=id_doproduto)
            novo_nome = request.POST['nomeproduto']
            nova_imagem = request.FILES.get('imagemproduto', False)
            if nova_imagem:
                deleta = item.imagem.path
                os.remove(deleta)
                item.imagem = nova_imagem
            if novo_nome == '':
                pass
            else:
                item.nome_do_produto = novo_nome
  
            item.save()
            direcionamento_imagem.imagem_caminho_produto(item.nome_do_produto)

            messages.success(request, 'Produto alterado com sucesso.')
            return redirect('editaproduto', id_doproduto)

        return render(request, 'manutencao_templates/editaproduto.html', dados)
    else:
        return redirect('login')

def deltando_produto(request, id_doproduto):

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:
        
        produto = get_object_or_404(Iten, pk=id_doproduto) 
        id_decategoria = produto.categoria.id
        deleta = produto.imagem.path
        if os.path.exists(deleta):
            os.remove(deleta)
        produto.delete()
        return redirect('editaprodutos', id_decategoria)

    else:
        return redirect('login')