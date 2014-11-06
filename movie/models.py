from django.db import models

class Movie(models.Model):
    url = models.CharField(max_length=500, blank=False, null=False)
    categoria = models.IntegerField(null=False)
    descricao = models.CharField(max_length=300, blank=True)

class Categoria(models.Model):
    descricao = models.CharField(max_length=300, blank=True)

class ComentsForMovie(models.Model):
	id_Movie = models.IntegerField(null=False, blank=False)
	comentarios = models.CharField(max_length=500, null=True, blank=True)	
	dataCadastro = models.DateTimeField(null=False, auto_now=True)

class LikesForMovie(models.Model):
	id_Movie = models.IntegerField(null=False, blank=False)
	like = models.IntegerField(null=True, default=0)	
	unlike = models.IntegerField(null=True, default=0)

'''class Pessoa(models.Model):
	nome = models.CharField('Login',max_length=100)
	email = models.EmailField() 
	senha = models.CharField(max_length=15)'''