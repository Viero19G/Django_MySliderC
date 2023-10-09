# custom_filters.py
from django import template

register = template.Library()

### filtro para identificar os videos se são mp4
@register.filter(name='url_endswith_mp4')
def url_endswith_mp4(value):
    return value.endswith('.mp4')


@register.filter
def multiply(value, arg):
    try:
        # antes de multiplicar, value é convertido em um número de ponto flutuante usando float(value)
        value_as_number = float(value)
        return value_as_number * arg
    except (ValueError, TypeError):
        return ''
