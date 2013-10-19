from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from node_registration import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^about/', views.AboutView.as_view()),
	url(r'^admin/', include(admin.site.urls)),
	url(r'position', include('node_registration.urls')),
)

