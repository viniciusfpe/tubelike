from django.db import models

class Movie(models.Model):
    url = models.CharField(max_length=500, blank=False, null=False)
    categoria = models.IntegerField(null=False, blank=True)
    descricao = models.CharField(max_length=300, blank=True)
    like = models.IntegerField(null=True, blank=True, default=0)

class Categoria(models.Model):
    descricao = models.CharField(max_length=300, blank=True)


