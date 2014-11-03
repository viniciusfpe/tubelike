from django import forms
from movie.models import Movie, ComentsForMovie

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie

class ComentsForMovieForm(forms.ModelForm):
	class Meta:
		model = ComentsForMovie