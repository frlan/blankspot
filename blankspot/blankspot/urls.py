from django.conf.urls import patterns, include, url
from django.contrib import admin
from node_registration import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blankspot.views.home', name='home'),
    # url(r'^blankspot/', include('blankspot.foo.urls')),
    url(r'^list/', views.list_nodes, name='node_list'),
    url(r'^$', views.index, name='index'),
    url(r'^$', include('node_registration.urls')),
    url(r'^register/', include('node_registration.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
