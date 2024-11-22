from Cleanzy.products.models import Product
from django.conf import settings

user = settings.AUTH_USER_MODEL  # Reference it dynamically


def get_account(context):
    request = context.get('request')
    if request and hasattr(request, 'user'):
        return request.user.is_authenticated
    return False


def get_products():
    return Product.objects.all().get()