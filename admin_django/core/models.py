from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=120)
    preco = models.IntegerField()
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome
    
    