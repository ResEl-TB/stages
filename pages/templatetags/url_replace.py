from urllib.parse import urlencode
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, page):
    query = context['request'].GET.dict()
    query.update({'page': page})
    return urlencode(query)