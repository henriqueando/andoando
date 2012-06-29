from django.views.generic import TemplateView, ListView
from .models import Noticia

class HomeView(TemplateView):
    template_name = 'noticiario/fluid.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        if 'secao' in kwargs:
            noticias = Noticia.objects.filter(secao=kwargs['secao'])
            context ['secao_atual'] = kwargs['secao']
        else:
            noticias = Noticia.objects.all()
            context ['secao_atual'] = 'home'

        context['destaque_primario'] = noticias.filter(destaque=1).latest()        
        ultimas = noticias.filter(destaque=2)[:6]        
        destaques_secundarios = [ultimas[:3], ultimas[3:6]] 
        context ['destaques_secundarios'] = destaques_secundarios   
        context ['secoes'] = Noticia.secoes_existentes()     
        return context
    
class ListaSecaoView(ListView):
        paginate_by = 5
        def get_queryset(self):
            return Noticia.objects.filter(secao=self.kwargs['secao'])
        

        

