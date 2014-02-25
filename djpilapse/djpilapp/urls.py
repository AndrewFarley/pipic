from django.conf.urls import patterns, url

from djpilapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url('^shoot/(\d+)/(\d+)/$', views.shoot, name='shoot'),
    url('^newProject/(\d+)/(\d+)/$', views.newProject, name='newProject'),
)
