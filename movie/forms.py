from django import forms
from movie.models import Movie, LikeComentsForMovie

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie

class LikeComentsForMovieForm(forms.ModelForm):
	class Meta:
		model = LikeComentsForMovie