from django.shortcuts import render
from produtos.models import Categoria

def index(request):

    categorias = Categoria.objects.all()

    dados = {
        'categorias' : categorias
    }

    return render(request,'index.html', dados)
