from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.manutencao, name='manutencao'),
    path('dados', views.dados, name='dados'),
    path('sobre', views.sobre, name='sobre'),
    path('imagenssite', views.imagenssite, name='imagenssite'),
    path('categoria', views.categoria, name='categoria'),
    path('editacategoria/<int:id_decategoria>', views.editacategoria, name='editacategoria'),
    path('deletandocategoria/<int:id_decategoria>', views.deletando_categoria, name='deletando_categoria'),
    path('produto', views.produto, name='produto'),
    path('editaprodutos/<int:id_decategoria>', views.editaprodutos, name='editaprodutos'),
    path('editaproduto/<int:id_doproduto>', views.editaproduto, name='editaproduto'),    
    path('deletandoproduto/<int:id_doproduto>', views.deltando_produto, name='deltando_produto'),
]