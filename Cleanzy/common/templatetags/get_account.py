from django import template

from Cleanzy.utils import get_account

register = template.Library()

@register.simple_tag
def get_current_account():
    return get_account()