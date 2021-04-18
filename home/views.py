from django.shortcuts import render
from produtos.models import Iten

def index(request):

    produtos = Iten.objects.all()

    dados = {
        'produtos' : produtos
    }

    return render(request,'index.html', dados)
