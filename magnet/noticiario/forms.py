from django import forms

from .models import Noticia

class FormContato (forms.Form):
    nome = forms.CharField()
    email = forms.EmailField()
    texto = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        import json
        with open('emails.json', 'ab') as arq_emails:
            json.dump(self.cleaned_data, arq_emails, indent=2)
            arq_emails.write('\n')

class FormNoticia (forms.ModelForm):
    class Meta:
        model = Noticia 
