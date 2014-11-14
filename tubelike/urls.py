""" 
@vfpeixoto
@polianacavazini
"""

from django.conf.urls import patterns, include, url
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('movie.views',
	url(r'^hello/$', 'hello'),
    url(r'^$', 'index'),
    url(r'^cadastro/$', 'cadastro'),
    url(r'^cadastrar/$', 'cadastrar'),
    url(r'^videos/(?P<c>\d+)/$', 'getMovie'),
    url(r'^video/(?P<v>\d+)/$', 'getMovieForComents'),
    url(r'^like/(?P<pk>\d+)/$', 'like'),
    url(r'^unlike/(?P<pk>\d+)/$', 'unlike'),
    url(r'^comentar/(?P<pk>\d+)/$', 'comments'),
    url(r'^LikesUnlikes/(?P<pk>\d+)/$', 'getLikesUnlikesForMovie'),
    url(r'^login/$', 'login'),
    url(r'^validar/$', 'validar'),
    url(r'^logoff/$', 'logoff'),
    url(r'^Cadastrouser/$', 'Cadastro_user'),
    url(r'^Cadastraruser/$', 'Cadastrar_user'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)