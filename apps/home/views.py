from django.shortcuts import render
from produtos.models import Categoria, Iten
from manutencao.models import Empresa, Imagem_site

def index(request):
    ''' View do index (pagina inicial) '''

    categorias = Categoria.objects.all().order_by('nome_da_categoria')
    produtos = Iten.objects.all().order_by('nome_do_produto')
    
    try:
        empresa = Empresa.objects.get(pk=1)
    except Empresa.DoesNotExist:
        empresa = None

    try:
        carrosseis = Imagem_site.objects.filter(rodape=False)
    except Imagem_site.DoesNotExist:
        carrosseis = None

    try:
        rodape = Imagem_site.objects.filter(rodape=True)
    except Imagem_site.DoesNotExist:
        rodape = None
        
    dados = {
        'categorias' : categorias,
        'produtos'   : produtos,
        'empresa'    : empresa,
        'rodape'     : rodape,
        'carrosseis'  : carrosseis,
    }

    return render(request,'index.html', dados)
