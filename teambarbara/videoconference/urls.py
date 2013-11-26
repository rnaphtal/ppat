from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from videoconference import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^create/', views.create_user),
    url(r'^welcome', views.welcome),
    url(r'^meeting/(.*)', views.login, name='meeting room'),
    url(r'^participants/(.*)',views.get_participants),
    url(r'^get_videoID/(.*)',views.get_videoID),
    url(r'^deleteUser/(.*)',views.deleteUser),
    url(r'^set_videoID/(?P<p_name>\w+)/(?P<p_id>\w+)',views.set_videoID),
    #url(r'^meeting/(.*)', views.enterRoom, name='meeting room'),
)
