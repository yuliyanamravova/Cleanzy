from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Cleanzy.companies.models import Company
from Cleanzy.companies.forms import AddCompanyForm, DeleteCompanyForm, EditCompanyForm


# Create your views here.


class AddCompanyView(CreateView):
    template_name = 'companies/company-add.html'
    model = Company
    success_url = reverse_lazy('home')
    form_class = AddCompanyForm
    permission_required = 'companies.add_companies'

    def get_success_url(self):
        return reverse_lazy('detail-company', kwargs={'pk': self.object.pk})


class DeleteCompanyView(PermissionRequiredMixin, DeleteView):
    template_name = 'companies/company-delete.html'
    model = Company
    success_url = reverse_lazy('home')
    form_class = DeleteCompanyForm
    permission_required = 'companies.delete_companies'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class EditCompanyView(UpdateView):
    template_name = 'companies/company-edit.html'
    model = Company
    success_url = reverse_lazy('home')
    form_class = EditCompanyForm
    permission_required = 'companies.change_companies'

    def get_success_url(self):
        return reverse_lazy('detail-company', kwargs={'pk': self.object.pk})


class DetailCompanyView(DetailView):
    template_name = 'companies/company-details.html'
    model = Company
    permission_required = 'companies.view_companies'
