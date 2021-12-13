from django.db import models

class Empresa(models.Model):

    nome_da_empresa = models.CharField(max_length=50, null=True)
    ddd = models.CharField(max_length=3, null=True)
    telefone1 = models.CharField(max_length=15, null=True)
    telefone2 = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    endereco = models.CharField(max_length=200, null=True)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=2, null=True)
    geo_localizacao = models.URLField(max_length=500, null=True)
    texto = models.TextField(null=True)
    logo = models.ImageField(upload_to='temp/', null=True)
    
    def __str__(self):
        return self.nome_da_empresa 

class Imagem_site(models.Model):

    imagem = models.ImageField(upload_to='temp/')
    rodape = models.BooleanField(default=False)