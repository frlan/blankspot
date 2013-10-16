from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from node_registration import views
from node_registration.views import PositionCreate, PositionDelete, PositionUpdate



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^about/', views.AboutView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'position/add/$', PositionCreate.as_view(), name='position_add'),
    url(r'position/(?P<pk>\d+)/$', PositionUpdate.as_view(), name='position_update'),
    url(r'position/(?P<pk>\d+)/delete/$', PositionDelete.as_view(), name='position_delete'),
    #url(r'^register/$', views.RegisterForm.as_view()),
    #url(r'^registering/$', views.Register.as_view()),
)

#~ urlpatterns = patterns('',
    #~ # Examples:
    #~ # url(r'^$', 'blankspot.views.home', name='home'),
    #~ # url(r'^blan	kspot/', include('blankspot.foo.urls')),
    #~ url(r'^list/', views.list_nodes, name='node_list'),
    #~ url(r'^about/', TemplateView.as_view(template_name="about.html")),
    #~ url(r'^$', views.index, name='index'),
    #~ url(r'^$', include('node_registration.urls')),
    #~ url(r'^about/', TemplateView.as_view(template_name="about.html")),
    #~ url(r'^register/', include('node_registration.urls')),
	#~ url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #~ url(r'^admin/', include(admin.site.urls)),
#~ )
