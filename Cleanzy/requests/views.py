from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from Cleanzy.requests.forms import CreateRequestForm, DeleteRequestForm, EditRequestForm
from Cleanzy.requests.models import Request


# Create your views here.

class CreateRequestView(CreateView):
    model = Request
    form_class = CreateRequestForm
    success_url = reverse_lazy('details-request', kwargs={'pk'})
    template_name = 'requests/request-create.html'

    def form_valid(self, form):
        request = form.save(commit=False)
        request.user = self.request.user
        request.save()
        return super().form_valid(form)


class DeleteRequestView(DeleteView):
    model = Request
    form_class = DeleteRequestForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'


class DetailRequestView(DetailView):
    pk_url_kwarg = 'id'
    model = Request


class EditRequestView(UpdateView):
    pk_url_kwarg = 'id'
    model = Request
    form_class = EditRequestForm
    success_url = reverse_lazy('home')


class ListRequestView(ListView):
    paginate_by = 4
    template_name = 'requests/request-list.html'
    model = Request
    context_object_name = 'requests'
