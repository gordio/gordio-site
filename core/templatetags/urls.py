from django import template
from django.core.urlresolvers import reverse


register = template.Library()


@register.simple_tag(takes_context=True)
def url_active(context, url, hard=True):
    """
        Usage:
        {% active <urls_name> <equivalent:default=True> %}
        {% active 'admin:login' %}
        {% active 'admin:home' False %}
    """
    request = context['request']
    url = reverse(url)
    if hard:
        if request.path == url:
            return 'active'
    else:
        if request.path.startswith(url):
            return 'active'
    return ''
