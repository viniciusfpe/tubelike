""" 
@vfpeixoto
@polianacavazini
"""

# coding: utf-8
from django import forms
from movie.models import Movie, ComentsForMovie
from movie.models import Pessoa

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie

class ComentsForMovieForm(forms.ModelForm):
	class Meta:
		model = ComentsForMovie

class PessoaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Pessoa

class LoginForm(forms.Form):
    login = forms.CharField(max_length=100, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)