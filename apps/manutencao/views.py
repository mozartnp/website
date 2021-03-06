import os
import shutil

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Empresa, Imagem_site
from produtos.models import Categoria, Iten
from extra import direcionamento_imagem

def manutencao(request):
    ''' View para pagina inical da manutenção '''

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:
        return render(request, 'manutencao.html')
    else:
        return redirect('login')

def dados(request):
    ''' Pagina de edição dos dados da empresa do site '''

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        if request.method =='POST':
            nomedaempresa = request.POST['nomedaempresa']
            ddd = request.POST['ddd']
            telefone1 = request.POST['telefone1']
            telefone2 = request.POST['telefone2']
            email = request.POST['email']
            endereco = request.POST['endereco']
            estado = request.POST['estado']
            cidade = request.POST['cidade']
            geoloca = request.POST['geoloca']
            nova_imagem = request.FILES.get('logo', False)
            
            try:
                empresa = Empresa.objects.get(pk=1)
            except Empresa.DoesNotExist:
                var_temp = Empresa(id=1)
                var_temp.save()
                empresa = Empresa.objects.get(pk=1)

            if nova_imagem:
                empresa.logo = nova_imagem
                #TODO arrumar a questão se tiver outra imagem, para não gerar muito lixo

            #TODO arrumar validações, para por exemplo não passar valor vazio.
            empresa.nome_da_empresa = nomedaempresa
            empresa.ddd = ddd
            empresa.telefone1 = telefone1
            empresa.telefone2 = telefone2
            empresa.email = email
            empresa.endereco = endereco
            empresa.estado = estado
            empresa.cidade = cidade 
            empresa.geo_localizacao = geoloca

            empresa.save()
            direcionamento_imagem.imagem_logo_caminho()

        return render(request, 'manutencao_templates/dadosempresa.html')
    else:
        return redirect('login')

def sobre(request):
    ''' Pagina de edição do texto "sobre nos" e das imagens que compõe o site '''

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        if request.method == 'POST':
            texto = request.POST['empresatexto']
            
            try:
                empresa = Empresa.objects.get(pk=1)
            except Empresa.DoesNotExist:
                var_temp = Empresa(id=1)
                var_temp.save()
                empresa = Empresa.objects.get(pk=1)

            empresa.texto = texto

            empresa.save()
        
        else:
            try:
                carrosseis = Imagem_site.objects.filter(rodape=False)
                contexto = {
                    'carrosseis' : carrosseis,
                }
                return render(request, 'manutencao_templates/sobrenos.html', contexto)
            except Imagem_site.DoesNotExist:
                pass
        
        return render(request, 'manutencao_templates/sobrenos.html')
    else:
        return redirect('login')

def imagenssite(request):
    ''' View puramente para organizar as imagens do carrossel, ou do rodape'''
    
    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        if request.method == 'POST':
            imagemcarrossel = request.FILES.get('imagemcarrossel', False)
            imagemrodape = request.FILES.get('imagemrodape', False)

            if imagemcarrossel:
                Imagem_site.objects.create(imagem=imagemcarrossel)
                idimagem = Imagem_site.objects.order_by('id').reverse()[:1]
                direcionamento_imagem.imagem_site(idimagem[0].id)

            if imagemrodape:
                try:
                    imagemantiga = Imagem_site.objects.get(rodape=True)
                    deleta = imagemantiga.imagem.path
                    if os.path.exists(deleta):
                        os.remove(deleta)

                    imagemantiga.delete()

                except Imagem_site.DoesNotExist:
                    pass

                Imagem_site.objects.create(imagem=imagemrodape, rodape=True)
                idimagem = Imagem_site.objects.get(rodape=True)
                direcionamento_imagem.imagem_site(idimagem.id)
    

        return redirect('sobre')

def deletando_imagem_site(request, id_imagem):
    
    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:
        imagemsite = get_object_or_404(Imagem_site, pk=id_imagem) 
        deleta = imagemsite.imagem.path
        if os.path.exists(deleta):
            os.remove(deleta)
        imagemsite.delete()
        return redirect('sobre')

    else:
        return redirect('login')

def categoria(request):
    ''' Pagina para criar e acessar as categorias '''

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        categorias = Categoria.objects.all().order_by('nome_da_categoria')

        paginator = Paginator(categorias, 10)
        page = request.GET.get('page')
        categorias_por_pagina = paginator.get_page(page)

        dados = {
            'categorias' : categorias_por_pagina
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
    ''' Pagina para editar a categoria '''

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
    ''' View para deletar a categoria, e os produtos da categoria '''

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
    ''' Pagina para escolher a categoria que a pessoa quer criar/editar os produtos '''

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        categorias = Categoria.objects.all().order_by('nome_da_categoria')

        paginator = Paginator(categorias, 10)
        page = request.GET.get('page')
        categorias_por_pagina = paginator.get_page(page)

        dados = {
            'categorias' : categorias_por_pagina
        }

        return render(request, 'manutencao_templates/produto.html', dados)
    else:
        return redirect('login')

def editaprodutos(request, id_decategoria):
    ''' Pagina para criar produtos dentro de uma determinada categoria, ou abrir um produto para editar '''

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        categoria = get_object_or_404(Categoria, pk=id_decategoria) 
        produtos = Iten.objects.filter(categoria=categoria).order_by('nome_do_produto')

        paginator = Paginator(produtos, 10)
        page = request.GET.get('page')
        produtos_por_pagina = paginator.get_page(page)

        dados = {
            'categoria' : categoria ,
            'produtos' : produtos_por_pagina,
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
    ''' Pagina para editar um determinado produto '''

    #Verificação de usuario para poder usar ou não a tela de manutencao
    if request.user.is_authenticated:

        produto = get_object_or_404(Iten, pk=id_doproduto) 
        
        dados = {
            'produto' : produto
        }  

        if request.method == 'POST':

            item = Iten.objects.get(pk=id_doproduto)
            catego = Categoria.objects.get(pk=item.categoria.id)
            id_decategoria = catego.id

            novo_nome = request.POST['nomeproduto']
            nova_imagem = request.FILES.get('imagemproduto', False)
            capa_va = request.POST.get('checkdacapa', False)

            if nova_imagem:
                deleta = item.imagem.path
                os.remove(deleta)
                item.imagem = nova_imagem

            if novo_nome != '':
                item.nome_do_produto = novo_nome
          
            if capa_va != item.capa:
                if capa_va == 'on' and item.capa == False:
                    item.capa = True
                    
                    if catego.produto_de_capa != None:
                        outroitem = catego.produto_de_capa.id
                        Iten.objects.filter(id=outroitem).update(capa=False)

                    Categoria.objects.filter(id=id_decategoria).update(produto_de_capa=id_doproduto)
                               
            item.save()
            direcionamento_imagem.imagem_caminho_produto(item.nome_do_produto)

            messages.success(request, 'Produto alterado com sucesso.')
            return redirect('editaproduto', id_doproduto)

        return render(request, 'manutencao_templates/editaproduto.html', dados)
    else:
        return redirect('login')

def deltando_produto(request, id_doproduto):
    ''' View para deletar um produto '''

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