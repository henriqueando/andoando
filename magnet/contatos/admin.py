# coding: utf-8

from django.contrib import admin

from .models import Contato, Fone

class FoneInline (admin.TabularInline):
    model = Fone

class ContatoAdmin (admin.ModelAdmin):
    inlines = (FoneInline, )


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Fone)

