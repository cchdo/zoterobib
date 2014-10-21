from django.conf.urls import patterns, url

from zoterobib import views

urlpatterns = patterns('',
        url(r'^$', views.index, name="index"),
        url(r'^bibliography.json$', views.load, name="load"),
        )
