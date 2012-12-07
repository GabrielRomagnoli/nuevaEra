from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('musica.views',
    url(r'^$', 'index', name="musica_index"),
    url(r'^(?P<tema_id>\d+)/$', 'detalle', name="musica_detalle"),
    url(r'^(?P<tema_id>\d+)/comentar/$', 'comentar', name="musica_comentar"),
)