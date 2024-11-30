from django import forms

from Cleanzy.warehouses.models import Warehouse


class WarehouseBaseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'
        labels = {
            'town': 'Town',
            'phone_number': 'Phone Number',
            'address': 'Address',
            'products': 'Products'
        }


class AddWarehouseForm(WarehouseBaseForm):
    pass


class EditWarehouseForm(WarehouseBaseForm):
    pass


class DeleteWarehouseForm(WarehouseBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True

