from django.conf.urls import patterns, url

from videoconference import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
