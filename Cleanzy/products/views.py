from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from Cleanzy.products.forms import CreateProductForm, DeleteProductForm, EditProductForm
from Cleanzy.products.models import Product


def catalogue(request):
    return render(request, 'products/catalogue.html')


class CreateProductView(CreateView):
    model = Product
    form_class = CreateProductForm
    success_url = reverse_lazy('home')
    template_name = 'products/product-create.html'


class DeleteProductView(DeleteView):
    model = Product
    form_class = DeleteProductForm
    success_url = reverse_lazy('home')
    template_name = 'products/product-delete.html'
    pk_url_kwarg = 'pk'


class DetailProductView(DetailView):
    template_name = 'products/product-details.html'
    pk_url_kwarg = 'pk'
    model = Product


class EditProductView(UpdateView):
    template_name = 'products/product-edit.html'
    pk_url_kwarg = 'pk'
    form_class = EditProductForm
    model = Product
