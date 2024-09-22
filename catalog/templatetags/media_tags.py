from django import template
from django.conf import settings

register = template.Library()


@register.filter(name="mymedia")
def mymedia(data):
    if data:
        return f"{settings.MEDIA_URL}{data}"
    return "#"
