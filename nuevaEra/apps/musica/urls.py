from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('musica.views',
    url(r'^$', 'index'),
    url(r'^(?P<tema_id>\d+)/$', 'detalle'),
    url(r'^(?P<tema_id>\d+)/comentar/$', 'comentar'),
)