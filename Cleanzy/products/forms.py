from django import forms

from Cleanzy.products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CreateProductForm(ProductForm):
    pass


class DeleteProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = True


class EditProductForm(ProductForm):
    pass