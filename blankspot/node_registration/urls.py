from django.conf.urls import patterns, url

from node_registration import views

urlpatterns = patterns('',
    url(r'^$', views.list_nodes, name='node_list'),
    url(r'^$', views.index, name='index'),
)
