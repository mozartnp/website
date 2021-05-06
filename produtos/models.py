from django.db import models

class Categoria(models.Model):
    nome_da_categoria = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.nome_da_categoria

class Iten(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome_do_produto = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to='fotos/%d/%m/%Y')