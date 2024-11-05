from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView

from Cleanzy.accounts.forms import CreateAccountForm, DeleteAccountForm, EditAccountForm, LoginAccountForm
from Cleanzy.accounts.models import Account


# Create your views here.

class CreateAccountView(CreateView):
    model = Account
    form_class = CreateAccountForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/account-create.html'


class EditAccountView(UpdateView):
    model = Account
    form_class = EditAccountForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/account-edit.html'
    pk_url_kwarg = 'id'


class DeleteAccountView(DeleteView):
    model = Account
    form_class = DeleteAccountForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/account-delete.html'
    pk_url_kwarg = 'id'


def details_account(request, id):
    account = Account.objects.get(id=id)
    context = {
        'account': account,
    }
    return render(request, 'accounts/account-details.html', context=context)


def log_in_account(request):
    form = LoginAccountForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/account-log-in.html', context=context)


def log_out_account(request, id):

    return render(request, 'accounts/account-log-out.html')
