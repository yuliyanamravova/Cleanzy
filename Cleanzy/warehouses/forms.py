from django import forms

from Cleanzy.warehouses.models import Warehouse


class WarehouseBaseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'


class AddWarehouseForm(WarehouseBaseForm):
    pass


class EditWarehouseForm(WarehouseBaseForm):
    pass


class DeleteWarehouseForm(WarehouseBaseForm):
    pass
