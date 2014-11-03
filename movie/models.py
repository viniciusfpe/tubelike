from django.db import models

class Movie(models.Model):
    url = models.CharField(max_length=500, blank=False, null=False)
    categoria = models.IntegerField(null=False)
    descricao = models.CharField(max_length=300, blank=True)

class Categoria(models.Model):
    descricao = models.CharField(max_length=300, blank=True)

class LikeComentsForMovie(models.Model):
	id_Movie = models.IntegerField(null=False, blank=False)
	comentarios = models.CharField(max_length=500, null=True, blank=True)
	likes = models.IntegerField(null=False, blank=False)
	dataCadastro = models.DateField(null=False)