from django.views.generic import TemplateView
from .models import Noticia

class HomeView(TemplateView):
    template_name = 'noticiario/fluid.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['destaque_primario'] = Noticia.objects.latest()        
        return context
