from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def manutencao(request):
    return render(request, 'manutencao.html')

def logout(request):
    pass
