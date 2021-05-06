from django.shortcuts import render
from produtos.models import Categoria, Iten

def index(request):

    categorias = Categoria.objects.all()
    produtos = Iten.objects.all()

    dados = {
        'categorias' : categorias,
        'produtos' : produtos
    }

    return render(request,'index.html', dados)
