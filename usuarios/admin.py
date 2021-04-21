from django.contrib import admin
from .models import Usuario

class ListandoUsuario(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')

admin.site.register(Usuario, ListandoUsuario)