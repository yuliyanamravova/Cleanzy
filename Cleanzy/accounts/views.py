from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from Cleanzy.accounts.forms import CreateAccountForm, DeleteAccountForm, EditAccountForm
from Cleanzy.accounts.models import Account


# Create your views here.

class CreateAccountView(CreateView):
    model = Account
    form_class = CreateAccountForm
    success_url = reverse_lazy('details-account')
    template_name = 'accounts/account-create.html'


class EditAccountView(UpdateView):
    model = Account
    form_class = EditAccountForm
    success_url = reverse_lazy('details-account')
    template_name = 'accounts/account-edit.html'


class DeleteAccountView(DeleteView):
    model = Account
    form_class = DeleteAccountForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/account-delete.html'


def details_account(request, pk):
    return render(request, 'accounts/account-details.html')


def log_in_account(request):
    return render(request, 'accounts/account-log-in.html')


def log_out_account(request, pk):
    return render(request, 'accounts/account-log-out.html')
