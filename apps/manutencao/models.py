from django.db import models

class TextoEmpresa(models.Model):
    texto = models.TextField()
    def __str__(self):
        return self.texto