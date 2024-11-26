from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from Cleanzy.requests.forms import CreateRequestForm, DeleteRequestForm, EditRequestForm
from Cleanzy.requests.models import Request


# Create your views here.

class CreateRequestView(LoginRequiredMixin, CreateView):
    model = Request
    form_class = CreateRequestForm
    template_name = 'requests/request-create.html'
    success_url = reverse_lazy('list-request')
    login_url = 'login'
    redirect_field_name = 'next'

    def form_valid(self, form):
        request = form.save(commit=False)
        request.author = self.request.user
        return super().form_valid(form)


class DeleteRequestView(DeleteView):
    model = Request
    form_class = DeleteRequestForm
    success_url = reverse_lazy('list-request')
    template_name = 'requests/request-delete.html'
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class DetailRequestView(DetailView):
    pk_url_kwarg = 'id'
    model = Request


class EditRequestView(UpdateView):
    pk_url_kwarg = 'id'
    model = Request
    form_class = EditRequestForm
    template_name = 'requests/request-edit.html'
    success_url = reverse_lazy('list-request')


class ListRequestView(ListView):
    paginate_by = 4
    template_name = 'requests/request-list.html'
    model = Request
    context_object_name = 'requests'
