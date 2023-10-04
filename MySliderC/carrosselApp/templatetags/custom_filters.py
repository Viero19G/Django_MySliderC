# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='url_endswith_mp4')
def url_endswith_mp4(value):
    return value.endswith('.mp4')
