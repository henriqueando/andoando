# coding: utf-8

from django.shortcuts import render, HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory

from .forms import ContatoSimples, FoneForm, ContatoModelForm, FoneModelForm
from .models import Contato, Fone


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

def contato_simples_com_modelform(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contatos/contato_ok.html', {'form':form})
    else: 
        form = ContatoSimples()
    
    return render(request, 'contatos/contato_simples.html', {
        'form': form,
    })


def contato_fones(request):
    FonesFormSet = formset_factory(FoneForm)
    if request.method == 'POST':
        form_contato = ContatoSimples(request.POST)
        forms_fones = FonesFormSet(request.POST)
        
        if form_contato.is_valid() and forms_fones.is_valid():
            contato = Contato(nome=form_contato.cleaned_data['nome'], email=form_contato.cleaned_data['email'])
            contato.save()
            for form_fone in forms_fones:
                fone = Fone(contato=contato, 
                            tipo=form_fone.cleaned_data['tipo'],
                            ddd=form_fone.cleaned_data['ddd'],
                            numero=form_fone.cleaned_data['numero'])
                fone.save() 
            
            return render(request, 'contatos/contato_ok.html', {'form_contato': form_contato, 'forms_fones': forms_fones})
    else: 
        form_contato = ContatoSimples()
        forms_fones = FonesFormSet()
    
    return render(request, 'contatos/contato_fones.html', {
        'form_contato': form_contato, 'forms_fones': forms_fones})


def contato_fones_com_modelform(request):
    FonesFormSet = inlineformset_factory(Contato, Fone)
    if request.method == 'POST':
        form_contato = ContatoModelForm(request.POST)        
        if form_contato.is_valid():
            contato = form_contato.save()            
            forms_fones = FonesFormSet(request.POST, instance=contato)
            if forms_fones.is_valid():
                forms_fones.save() 
            
            return render(request, 'contatos/contato_ok.html', {'form_contato': form_contato, 'forms_fones': forms_fones})
        else: 
            forms_fones = FonesFormSet(request.POST)

    else: 
        form_contato = ContatoModelForm()
        forms_fones = FonesFormSet()
    
    return render(request, 'contatos/contato_fones.html', {
        'form_contato': form_contato, 'forms_fones': forms_fones})



