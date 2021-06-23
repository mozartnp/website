import os
from produtos.models import Iten
from manutencao.models import Empresa, Imagem_site
from django.conf import settings
from django.shortcuts import get_object_or_404

def imagem_caminho_produto(nome):
    ''' Redireciona, e organiza o nome da imgem, para facilitar no catalogo delas, para produto '''

    produto = get_object_or_404(Iten, nome_do_produto=nome)
    caminho_inicial = produto.imagem.path

    final = produto.imagem.name.split('.')
    final = '.' + final[-1]
    produto.imagem.name = str(produto.categoria.id) + str(produto.id) + final

    caminho = settings.MEDIA_ROOT + '/fotos/' + str(produto.categoria.id)
    novo_caminho = caminho + '/' + str(produto.imagem.name)
    produto.imagem = 'fotos/' + str(produto.categoria.id) + '/' + str(produto.imagem.name)

    if os.path.exists(caminho) is False:
        os.mkdir(caminho)

    os.rename(caminho_inicial, novo_caminho)
    produto.save()

def imagem_logo_caminho():
    ''' Redireciona a imagem logo para o seu devido diretorio '''

    empresa = Empresa.objects.get(pk=1)
    caminho_inicial = empresa.logo.path

    final = empresa.logo.name.split('.')
    final = '.' + final[-1]
    empresa.logo.name = 'logo' + final    

    caminho = settings.MEDIA_ROOT + '/site'
    novo_caminho = caminho + '/' + str(empresa.logo.name)
    empresa.logo = 'site/' + str(empresa.logo.name)

    if os.path.exists(caminho) is False:
        os.mkdir(caminho)

    os.rename(caminho_inicial, novo_caminho)
    empresa.save()

def imagem_site(idimagem):
    """ Direciona e renomeia as imagems do carrossel e do rodape """
    
    imagem_a_tratar = Imagem_site.objects.get(pk=idimagem)
    caminho_inicial = imagem_a_tratar.imagem.path

    final = imagem_a_tratar.imagem.name.split('.')
    final = '.' + final[-1]
    if imagem_a_tratar.rodape == True:
        imagem_a_tratar.imagem.name = 'rodape' + str(imagem_a_tratar.id) + final
    elif imagem_a_tratar.rodape == False:
        imagem_a_tratar.imagem.name = 'carrossel' + str(imagem_a_tratar.id) + final

    caminho = settings.MEDIA_ROOT + '/site'
    novo_caminho = caminho + '/' + str(imagem_a_tratar.imagem.name)
    imagem_a_tratar.imagem = 'site/' + str(imagem_a_tratar.imagem.name)

    if os.path.exists(caminho) is False:
        os.mkdir(caminho)

    os.rename(caminho_inicial, novo_caminho)
    imagem_a_tratar.save()
