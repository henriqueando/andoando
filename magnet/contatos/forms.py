from django import forms

from .models import Contato, Fone, TIPOS_FONE

class ContatoSimples(forms.Form):
    nome = forms.CharField(max_length=128, help_text='Nome completo')
    email = forms.EmailField(help_text='Email principal')

class FoneForm(forms.Form):
    tipo = forms.ChoiceField(choices= TIPOS_FONE)
    ddd = forms.CharField(max_length=8, initial='5511')
    numero = forms.CharField(max_length=16)

class ContatoModelForm(forms.ModelForm):
    class Meta:
        model = Contato

class FoneModelForm(forms.ModelForm):
    class Meta:
        model = Fone
