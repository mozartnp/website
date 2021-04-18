from django.db import models

class Iten(models.Model):
    nome_do_produto = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
