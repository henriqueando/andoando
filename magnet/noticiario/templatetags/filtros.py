from django import template

register = template.Library()

@register.filter
def links(valor):
    return valor.upper()
