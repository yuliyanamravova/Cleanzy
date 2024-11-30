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

    def get_success_url(self):
        return reverse_lazy('detail-company', kwargs={'pk': self.object.pk})


class DeleteCompanyView(DeleteView):
    template_name = 'companies/company-delete.html'
    model = Company
    success_url = reverse_lazy('home')
    form_class = DeleteCompanyForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class EditCompanyView(UpdateView):
    template_name = 'companies/company-edit.html'
    model = Company
    success_url = reverse_lazy('home')
    form_class = EditCompanyForm

    def get_success_url(self):
        return reverse_lazy('detail-company', kwargs={'pk': self.object.pk})


class DetailCompanyView(DetailView):
    template_name = 'companies/company-details.html'
    model = Company
