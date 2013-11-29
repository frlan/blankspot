from django.conf.urls import patterns, url
from django.utils.translation import ugettext as _
from node_registration import views

urlpatterns = patterns('',
    url(r'^add/$', views.PositionCreate.as_view(), name='position-add'),
    url(r'^list', views.ListPosition.as_view(), name='position-list')
)
