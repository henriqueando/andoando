from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView, CreateView

from .models import Noticia

from .forms import FormContato, FormNoticia, FormContribNoticia



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
        

class ContatoView(FormView):
    template_name = 'noticiario/contato.html'
    form_class = FormContato
    success_url = '/grato/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContatoView, self).form_valid(form)
        
#class ContribuirView(FormView):
#    template_name = 'noticiario/contribuir.html'
#    form_class = FormNoticia
#    success_url = '/grato/'

class CriarNoticiaView(CreateView):
    model = Noticia
    form_class = FormContribNoticia
