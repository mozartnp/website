from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.manutencao, name='manutencao'),
    path('dados', views.dados, name='dados'),
    path('sobre', views.sobre, name='sobre'),
    path('categoria', views.categoria, name='categoria'),
    path('editacategoria/<int:id_decategoria>', views.editacategoria, name='editacategoria'),
    path('produto', views.produto, name='produto'),
]