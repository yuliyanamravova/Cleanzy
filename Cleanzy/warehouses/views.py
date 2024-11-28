from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from Cleanzy.warehouses.forms import AddWarehouseForm, EditWarehouseForm, DeleteWarehouseForm
from Cleanzy.warehouses.models import Warehouse


# Create your views here.


class AddWarehouseView(CreateView):
    form_class = AddWarehouseForm
    model = Warehouse
    success_url = reverse_lazy('home')
    template_name = 'warehouses/warehouse-add.html'


class EditWarehouseView(UpdateView):
    form_class = EditWarehouseForm
    model = Warehouse
    success_url = reverse_lazy('home')
    template_name = 'warehouses/warehouse-edit.html'


class DeleteWarehouseView(DeleteView):
    form_class = DeleteWarehouseForm
    model = Warehouse
    success_url = reverse_lazy('home')
    template_name = 'warehouses/warehouse-delete.html'


class DetailsWarehouseView(DetailView):
    model = Warehouse
    template_name = 'warehouses/warehouse-details.html'