from django import forms
#from pessoa.models import pessoas
from movie.models import Movie, ComentsForMovie

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie

class ComentsForMovieForm(forms.ModelForm):
	class Meta:
		model = ComentsForMovie

'''
class PessoaForm(forms.ModelForm):
	class Meta:
		model = pessoas
'''