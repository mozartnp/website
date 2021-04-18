from django.contrib import admin
from .models import Iten

class Listandoprodutos(admin.ModelAdmin):
    list_display = ('id', 'nome_do_produto')
    list_display_links = ('id', 'nome_do_produto')

admin.site.register(Iten, Listandoprodutos)