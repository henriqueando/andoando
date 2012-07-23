from django.conf.urls import patterns, include, url
from .views import contato_simples, contato_fones
from .views import contato_simples_com_modelform
from .views import contato_fones_com_modelform

urlpatterns = patterns('',
    url(r'^simples/$', contato_simples, name='form-contato-simples'),
    url(r'^simplesmf/$', contato_simples_com_modelform, name='modelform-contato-simples'),
    url(r'^fones/$', contato_fones, name='form-contato-fones'),
    url(r'^fonesmf/$', contato_fones_com_modelform, name='modelform-contato-fones'),
)
