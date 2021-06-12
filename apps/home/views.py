from django.shortcuts import render
from produtos.models import Categoria, Iten

def index(request):
    ''' View do index (pagina inicial) '''

    categorias = Categoria.objects.all().order_by('nome_da_categoria')
    produtos = Iten.objects.all().order_by('nome_do_produto')

    dados = {
        'categorias' : categorias,
        'produtos' : produtos
    }

    return render(request,'index.html', dados)
