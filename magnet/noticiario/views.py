from django.views.generic import TemplateView
from .models import Noticia

class HomeView(TemplateView):
    template_name = 'noticiario/fluid.html'
    def get_context_data(self, **kwargs):
        if 'secao' in kwargs:
            noticias = Noticia.objects.filter(secao=kwargs['secao'])
        else:
            noticias = Noticia.objects.all()
        context = super(HomeView, self).get_context_data(**kwargs)
        context['destaque_primario'] = noticias.filter(destaque=1).latest()        
        ultimas = noticias.filter(destaque=2)[:6]        
        destaques_secundarios = [ultimas[:3], ultimas[3:6]] 
        context ['destaques_secundarios'] = destaques_secundarios   
        context ['secoes'] = Noticia.secoes_existentes()     
        return context

