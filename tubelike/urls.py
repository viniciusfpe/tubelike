from django.conf.urls import patterns, include, url

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
)
