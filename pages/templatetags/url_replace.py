from urllib.parse import urlencode
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, page):
    request = context['request']
    search = {
        'zone': request.GET.get('zone', ''),
        'duree': request.GET.get('duree', ''),
        'domain': request.GET.getlist('domain', ''),
        'type_de_contrat': request.GET.get('type_de_contrat', ''),
        'nom_entreprise': request.GET.get('nom_entreprise', ''),
        'page': page,
    }
    return urlencode(search, True)