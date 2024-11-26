from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView



# Create your views here.
from django.conf import settings

from Cleanzy.accounts.forms import CleanzyUserCreationForm, CleanzyUserLoginForm

user = get_user_model()


class UserRegisterView(CreateView):
    model = user
    form_class = CleanzyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/account-register.html'

    """def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response"""


class UserLoginView(LoginView):
    form_class = CleanzyUserLoginForm
    template_name = 'accounts/account-log-in.html'


def details_account(request, pk):
    account = user.objects.get(pk=pk)
    context = {
        'user': account,
    }
    return render(request, 'accounts/account-details.html', context=context)

"""
class EditAccountView(UpdateView):
    pass
    #model = user
    #form_class = EditAccountForm
    #success_url = reverse_lazy('home')
    #template_name = 'accounts/account-edit.html'
    #pk_url_kwarg = 'id'


class DeleteAccountView(DeleteView):
    pass

    model = user
    form_class = DeleteAccountForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/account-delete.html'
    pk_url_kwarg = 'id'





def log_in_account(request):
    pass
    form = LoginAccountForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/account-log-in.html', context=context)


def log_out_account(request, id):
    pass
    return render(request, 'accounts/account-log-out.html')"""
