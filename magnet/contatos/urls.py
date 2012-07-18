from django.conf.urls import patterns, include, url
from .views import contato_simples

urlpatterns = patterns('',
    url(r'^simples/$', contato_simples, name='form-contato-simples'),
)
