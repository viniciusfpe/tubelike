from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('movie',
    url(r'^$', 'views.index'),
)
