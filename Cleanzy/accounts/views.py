from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
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


class UserDeleteView(DeleteView):
    model = user
    template_name = 'accounts/account-delete.html'
    success_url = 'home'

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user1 = self.get_object()
        user1.delete()
        return redirect(self.get_success_url())



class DetailsAccountView(DetailView):
    model = user
    template_name = 'accounts/account-details.html'
    pk_url_kwarg = 'pk'



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
