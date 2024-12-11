from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from Cleanzy.companies.models import Company
from Cleanzy.companies.forms import AddCompanyForm, DeleteCompanyForm, EditCompanyForm


# Create your views here.


class AddCompanyView(LoginRequiredMixin, CreateView):
    template_name = 'companies/company-add.html'
    model = Company
    success_url = reverse_lazy('home')
    form_class = AddCompanyForm

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        context = {
            'user': get_user_model()
        }
        return reverse_lazy('detail-company', kwargs={'pk': self.object.pk})


class DeleteCompanyView(LoginRequiredMixin, DeleteView):
    template_name = 'companies/company-delete.html'
    model = Company
    success_url = reverse_lazy('home')
    form_class = DeleteCompanyForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class EditCompanyView(LoginRequiredMixin, UpdateView):
    template_name = 'companies/company-edit.html'
    model = Company
    success_url = reverse_lazy('home')
    form_class = EditCompanyForm
    permission_required = 'companies.change_companies'

    def get_success_url(self):
        return reverse_lazy('detail-company', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)


class DetailCompanyView(LoginRequiredMixin, DetailView):
    template_name = 'companies/company-details.html'
    model = Company
    permission_required = 'companies.view_companies'

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to view this company.")
        return obj


