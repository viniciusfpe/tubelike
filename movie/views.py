from django.shortcuts import render, HttpResponseRedirect
from movie.forms import MovieForm, LikeComentsForMovieForm
from movie.models import Movie, Categoria, LikeComentsForMovie

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

	return HttpResponseRedirect('/cadastro/')


def getMovie(request, c=1):

	try:
		categorias = Categoria.objects.all().order_by('descricao')
		videos = Movie.objects.filter(categoria=c)
		return render(request, 'movie.html', {'videos':videos, 'categorias':categorias})

	except:
		return HttpResponseRedirect('/')


def getMovieForComents(request):

	idMovie = request.GET.get('m', '')

	if idMovie != '':
		try:
			movie = Movie.objects.get(pk=idMovie)
			#clmovie = LikeComentsForMovie.objects.Filter(id_Movie=id_Movie)

			return render(request, 'comentsmovie.html', {'movie':movie, 'clmovie':clmovie})

		except:
			return HttpResponseRedirect('/')

	else:
		return HttpResponseRedirect('/')