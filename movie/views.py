from django.shortcuts import render, HttpResponseRedirect
from movie.forms import MovieForm
from movie.models import Movie, Categoria

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