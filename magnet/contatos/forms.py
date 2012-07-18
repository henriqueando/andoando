from django import forms

class ContatoSimples(forms.Form):
    nome = forms.CharField(max_length=128, help_text='Nome completo')
    email = forms.EmailField(help_text='Email principal')
