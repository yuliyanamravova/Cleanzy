from django import forms

from Cleanzy.products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductForm(ProductForm):
    pass


class DeleteProductForm(ProductForm):
    pass


class EditProductForm(ProductForm):
    pass