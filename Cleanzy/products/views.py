from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

from Cleanzy.products.forms import CreateProductForm, DeleteProductForm, EditProductForm
from Cleanzy.products.models import Product


class CatalogueView(ListView):
    template_name = 'products/catalogue.html'
    model = Product
    context_object_name = 'products'


class CreateProductView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = 'products/product-create.html'
    permission_required = 'products.add_products'

    def get_success_url(self):
        return reverse_lazy('details-product', kwargs={'pk': self.object.pk})


class DeleteProductView(PermissionRequiredMixin, DeleteView):
    model = Product
    form_class = DeleteProductForm
    template_name = 'products/product-delete.html'
    success_url = reverse_lazy('catalogue')
    permission_required = 'products.delete_products'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class DetailProductView(DetailView):
    template_name = 'products/product-details.html'
    model = Product
    context_object_name = 'product'


class EditProductView(PermissionRequiredMixin, UpdateView):
    template_name = 'products/product-edit.html'
    form_class = EditProductForm
    model = Product
    permission_required = 'products.change_products'

    def get_success_url(self):
        return reverse_lazy('details-product', kwargs={'pk': self.object.pk})
