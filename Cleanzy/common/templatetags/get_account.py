from django import template

from Cleanzy.utils import get_account

register = template.Library()

@register.simple_tag(takes_context=True)
def get_current_account(context):
    return get_account(context)