from django.conf.urls import patterns, include, url
from helping_hands_app import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helping_hands_site.views.home', name='home'),
    # url(r'^helping_hands_site/', include('helping_hands_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'helping_hands_app.views.index', name='index'),
    url(r'^events/', include('helping_hands_site.urls', namespace="events")),
    url(r'^(?P<event_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<event_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<event_id>\d+)/vote/$', views.vote, name='vote'),
)

