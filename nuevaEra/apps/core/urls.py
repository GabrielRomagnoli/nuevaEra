from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='core_home'),
    url(r'^registrar/', 'core.views.registrar', name='core_registrar'),
    url(r'^error/', 'core.views.error', name='core_error'),
)