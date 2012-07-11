# coding: utf-8

from django.contrib import admin

from .models import Noticia, Link

class LinkInline(admin.TabularInline):
    model = Link
    fields = ('titulo', 'url', 'ativo')

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['dt_criacao', 'publicado', 'destaque', 'secao', 'titulo']
    list_display_links = ['secao', 'titulo']
    list_editable = ['destaque']
    search_fields = ['titulo', 'resumo', 'corpo']
    list_filter = ['secao', 'destaque']
    date_hierarchy = 'dt_criacao'
    inlines = (LinkInline, )

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Link)

