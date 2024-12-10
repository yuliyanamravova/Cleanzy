from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
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
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        request = form.save(commit=False)
        request.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        context = {
            'user': get_user_model()
        }
        return reverse_lazy('details-request', kwargs={'id': self.object.pk})


class DeleteRequestView(LoginRequiredMixin, DeleteView):
    model = Request
    form_class = DeleteRequestForm
    success_url = reverse_lazy('list-request')
    template_name = 'requests/request-delete.html'
    pk_url_kwarg = 'id'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class DetailRequestView(LoginRequiredMixin, DetailView):
    pk_url_kwarg = 'id'
    model = Request
    template_name = 'requests/request-details.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

    def get_queryset(self):
        # Restrict queryset to requests authored by the logged-in user
        return Request.objects.filter(author=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.author != self.request.user:
            raise PermissionDenied("You do not have permission to view this request.")
        return obj


class EditRequestView(LoginRequiredMixin, UpdateView):
    pk_url_kwarg = 'id'
    model = Request
    form_class = EditRequestForm
    template_name = 'requests/request-edit.html'
    success_url = reverse_lazy('list-request')
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

    def get_success_url(self):
        return reverse_lazy('details-request', kwargs={'id': self.object.pk})

    def get_queryset(self):
        return Request.objects.filter(author=self.request.user)


class ListRequestView(LoginRequiredMixin, ListView):
    template_name = 'requests/request-list.html'
    model = Request
    context_object_name = 'requests'

    def get_queryset(self):
        return Request.objects.filter(author=self.request.user)
