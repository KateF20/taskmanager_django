from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def url(name, *args, **kwargs):
    for key, value in list(kwargs.items()):
        if value is None:
            del kwargs[key]

    return reverse(name, args=args, kwargs=kwargs)
