from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    descricao = models.CharField(max_length=250)
    preco = models.FloatField()
    categoria = models.CharField(max_length=50)

    foto_produto = models.ImageField(upload_to='fotos/', blank=True)
    

