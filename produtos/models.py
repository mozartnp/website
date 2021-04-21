from django.db import models

class Categoria(models.Model):
    nome_da_categoria = models.CharField(max_length=30)
    def __str__(self):
        return self.nome_da_categoria

class Iten(models.Model):
    nome_do_produto = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)