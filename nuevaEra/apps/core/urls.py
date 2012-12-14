from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='core_home'),
    url(r'^registrar/', 'core.views.registrar', name='core_registrar'),
    url(r'^error/', 'core.views.error', name='core_error'),
    url(r'^loguearse/', 'core.views.loguearse', name='core_loguearse'),
    url(r'^desloguearse/', 'core.views.desloguearse', name='core_desloguearse'),
)