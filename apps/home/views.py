from django.shortcuts import render
from produtos.models import Categoria, Iten
from manutencao.models import Empresa

def index(request):
    ''' View do index (pagina inicial) '''

    categorias = Categoria.objects.all().order_by('nome_da_categoria')
    produtos = Iten.objects.all().order_by('nome_do_produto')

    try:
        empresa = Empresa.objects.get(pk=1)
    except Empresa.DoesNotExist:
        empresa = None
        
    dados = {
        'categorias' : categorias,
        'produtos'   : produtos,
        'empresa'    : empresa,
    }

    return render(request,'index.html', dados)
