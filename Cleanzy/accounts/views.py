from django.shortcuts import render

# Create your views here.


def create_account(request):
    return render(request, 'accounts/account-create.html')


def delete_account(request, pk):
    return render(request, 'accounts/account-delete.html')


def details_account(request, pk):
    return render(request, 'accounts/account-details.html')


def edit_account(request, pk):
    return render(request, 'accounts/account-edit.html')


def log_in_account(request):
    return render(request, 'accounts/account-log-in.html')


def log_out_account(request, pk):
    return render(request, 'accounts/account-log-out.html')
