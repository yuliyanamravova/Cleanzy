from django import template

register = template.Library()


@register.filter
def placeholder(value, text):
    value.field.widget.attrs['placeholder'] = text
    return value


@register.filter
def has_group(user, group_names):
    group_list = [name.strip() for name in group_names.split(',')]
    return user.groups.filter(name__in=group_list).exists()
