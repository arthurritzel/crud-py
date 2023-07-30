from django.db import models

# Create your models here.
class produtos(models.Model):
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    preco = models.FloatField()
