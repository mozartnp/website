from django.urls import path 
from . import views 

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.manutencao, name='manutencao'),
    path('logout', views.logout, name='logout'),
]