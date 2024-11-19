from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

from Cleanzy.products.forms import CreateProductForm, DeleteProductForm, EditProductForm
from Cleanzy.products.models import Product


class CatalogueView(ListView):
    template_name = 'products/catalogue.html'
    model = Product
    paginate_by = 4
    context_object_name = 'products'


class CreateProductView(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'products/product-create.html'

    def get_success_url(self):
        return reverse_lazy('details-product', kwargs={'pk': self.object.pk})


class DeleteProductView(DeleteView):
    model = Product
    form_class = DeleteProductForm
    success_url = reverse_lazy('catalogue')
    template_name = 'products/product-delete.html'


class DetailProductView(DetailView):
    template_name = 'products/product-details.html'
    model = Product
    context_object_name = 'product'


class EditProductView(UpdateView):
    template_name = 'products/product-edit.html'
    form_class = EditProductForm
    model = Product

    def get_success_url(self):
        return reverse_lazy('details-product', kwargs={'pk': self.object.pk})
