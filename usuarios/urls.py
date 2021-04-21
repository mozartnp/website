from django.urls import path 
from . import views 

urlpatterns = [
    path('login', views.login, name='login'),
    path('manutencao', views.manutencao, name='manutencao'),
    path('logout', views.logout, name='logout'),
]