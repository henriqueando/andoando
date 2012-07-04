from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, TemplateView

from .views import HomeView, ListaSecaoView, ContatoView, CriarNoticiaView
from .models import Noticia

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^grato/$', TemplateView.as_view(template_name='noticiario/grato.html')),
    url(r'^contato/$', ContatoView.as_view(), name='form-contato'),
    url(r'^contrib/$', CriarNoticiaView.as_view(), name='form-contrib'),
    url(r'^(?P<secao>\w+)/$', HomeView.as_view(), name='capa-secao'),
    url(r'^(?P<secao>\w+)/todas/$', ListaSecaoView.as_view(model=Noticia), name='lista-secao'),
    url(r'^bits/(?P<pk>\d+)$', DetailView.as_view(model=Noticia), name='noticia-detalhe'),
)
