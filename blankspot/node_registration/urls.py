from django.conf.urls import patterns, url

from node_registration import views

urlpatterns = patterns('',
	url(r'add/$', views.PositionCreate.as_view(), name='position-add'),
	url(r'/(?P<pk>\d+)/$', views.PositionUpdate.as_view(), name='position-update'),
	url(r'/(?P<pk>\d+)/delete/$', views.PositionDelete.as_view(), name='position-delete'),
	url(r'/list', views.ListPosition.as_view(), name='position-list'),
)
