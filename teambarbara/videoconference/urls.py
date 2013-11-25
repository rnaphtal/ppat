from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from videoconference import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^create/', views.create_user),
    url(r'^meeting/(.*)', views.login, name='meeting room'),
    #url(r'^meeting/(.*)', views.enterRoom, name='meeting room'),
)
