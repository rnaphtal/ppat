from django.conf.urls import patterns, url

from videoconference import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^meeting/(.*)', views.enterRoom, name='meeting room'),
)
