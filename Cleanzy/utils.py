from Cleanzy.accounts.models import Account
from Cleanzy.products.models import Product


def get_account():
    return Account.objects.all().get()


def get_products():
    return Product.objects.all().get()