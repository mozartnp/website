from django.contrib import admin
from .models import Iten, Categoria

class Listandoprodutos(admin.ModelAdmin):
    list_display = ('id', 'nome_do_produto')
    list_display_links = ('id', 'nome_do_produto')

class ListandoCategorias(admin.ModelAdmin):
    list_display = ('id', 'nome_da_categoria')
    list_display_links = ('id', 'nome_da_categoria')

admin.site.register(Iten, Listandoprodutos)
admin.site.register(Categoria, ListandoCategorias)