from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('movie.views',
    url(r'^$', 'index'),
    url(r'^cadastro/$', 'cadastro'),
    url(r'^cadastrar/$', 'cadastrar'),
    url(r'^videos/(?P<c>\d+)/$', 'getMovie'),
)
