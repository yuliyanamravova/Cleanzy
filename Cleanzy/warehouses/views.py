from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from Cleanzy.decorators import in_group
from Cleanzy.warehouses.forms import AddWarehouseForm, EditWarehouseForm, DeleteWarehouseForm
from Cleanzy.warehouses.models import Warehouse


# Create your views here.
user = get_user_model()

class AddWarehouseView(PermissionRequiredMixin, CreateView):
    form_class = AddWarehouseForm
    model = Warehouse
    success_url = reverse_lazy('home')
    template_name = 'warehouses/warehouse-add.html'
    permission_required = 'warehouse.add_warehouse'

    def get_success_url(self):
        return reverse_lazy('detail-warehouse', kwargs={'pk': self.object.pk})


class EditWarehouseView(PermissionRequiredMixin, UpdateView):
    form_class = EditWarehouseForm
    model = Warehouse
    success_url = reverse_lazy('home')
    template_name = 'warehouses/warehouse-edit.html'
    permission_required = 'warehouse.change_warehouse'

    def get_success_url(self):
        return reverse_lazy('detail-warehouse', kwargs={'pk': self.object.pk})


class DeleteWarehouseView(PermissionRequiredMixin, DeleteView):
    form_class = DeleteWarehouseForm
    model = Warehouse
    success_url = reverse_lazy('home')
    template_name = 'warehouses/warehouse-delete.html'
    permission_required = 'warehouse.delete_warehouse'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class DetailsWarehouseView(PermissionRequiredMixin, DetailView):
    model = Warehouse
    template_name = 'warehouses/warehouse-details.html'
    permission_required = 'warehouses.view_warehouse'
