# coding: utf-8

from django.shortcuts import render, HttpResponseRedirect
from .forms import ContatoSimples
from .models import Contato

def contato_simples(request):
    if request.method == 'POST':
        form = ContatoSimples(request.POST)
        if form.is_valid():
            contato = Contato(nome=form.cleaned_data['nome'], email=form.cleaned_data['email'])
            contato.save()
            return render(request, 'contatos/contato_ok.html', {'form':form})
    else: 
        form = ContatoSimples()
    
    return render(request, 'contatos/contato_simples.html', {
        'form': form,
    })

