from django.db import models

# Create your models here.

class Instrumento_Cliente(models.Model):
    nome = models.CharField(max_length=120)
    #foto = models.ImageField() já retorna a altura e a largura
    caminho_arq = models.FileField(upload_to="img") 

    def __str__(self) -> str:
        return self.nome

