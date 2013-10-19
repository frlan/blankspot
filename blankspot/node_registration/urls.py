from django.conf.urls import patterns, url

from node_registration import views

urlpatterns = patterns('',
	url(r'add/$', views.PositionCreate.as_view(), name='position_add'),
	url(r'/(?P<pk>\d+)/$', views.PositionUpdate.as_view(), name='position_update'),
	url(r'/(?P<pk>\d+)/delete/$', views.PositionDelete.as_view(), name='position_delete'),
	url(r'/list', views.ListPosition.as_view()),
#    url(r'^$', views.list_nodes, name='node_list'),
#    url(r'^$', views.index, name='index'),
)
