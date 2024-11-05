from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from Cleanzy.requests.forms import CreateRequestForm, DeleteRequestForm, EditRequestForm
from Cleanzy.requests.models import Request


# Create your views here.

class CreateRequestView(CreateView):
    model = Request
    form_class = CreateRequestForm
    success_url = reverse_lazy('home')
    template_name = 'requests/request-create.html'


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


def list_request(request):
    return render(request, 'requests/request-list.html')
