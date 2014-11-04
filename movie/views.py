from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from movie.forms import MovieForm, ComentsForMovieForm
from movie.models import Movie, Categoria, ComentsForMovie, LikesForMovie
from datetime import datetime

def hello(request):
    return HttpResponse('Teste Ajax!')

def index(request):
    return render(request, 'index.html')

def cadastro(request):
	form = MovieForm()
	try:
		categorias = Categoria.objects.all().order_by('descricao')		

	except:
		categorias = 'Erro ao buscar as categorias'

	return render(request, 'cadastro.html', {'form':form, 'categorias':categorias})
	

def cadastrar(request):
	form = MovieForm(request.POST)

	if form.is_valid():
		form.save()

	return HttpResponseRedirect('/videos/'+str(form.cleaned_data['categoria'])+'/')


def getMovie(request, c=0):

	try:
		categorias = Categoria.objects.all().order_by('descricao')
		videos = Movie.objects.filter(categoria=c)

		return render(request, 'movie.html', {'videos':videos, 'categorias':categorias})

	except:
		return HttpResponseRedirect('/')


def getMovieForComents(request, v=0):
	try:
		movie = Movie.objects.get(pk=v)
		cmovie = ComentsForMovie.objects.filter(id_Movie=v)

		return render(request, 'comentsmovie.html', {'movie':movie, 'cmovie':cmovie})

	except:
		return HttpResponseRedirect('/')

def like(request, pk=0):
	try:
		like = LikesForMovie.objects.get(id_Movie=pk)
		likes = like.like + 1
	except:
		like = LikesForMovie()
		like.id_Movie = pk
		likes = 1

	like.like = likes
	like.save()

	return HttpResponse(likes)


def unlike(request, pk=0):
	try:
		like = LikesForMovie.objects.get(id_Movie=pk)
		unlikes = like.unlike + 1
	except:
		like = LikesForMovie()
		like.id_Movie = pk
		unlikes = 1

	
	like.unlike = unlikes
	like.save()

	return HttpResponse(unlikes)


def comments(request, pk=0):

	comentario = ComentsForMovie()
	comentario.id_Movie = pk
	comentario.comentarios = request.POST.get('text', '')

	comentario.save()	

	data = comentario.comentarios+";"+str(comentario.dataCadastro.strftime('%H:%M %d/%m/%y'))

	return HttpResponse(data)

	

