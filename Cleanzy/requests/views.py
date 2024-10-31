from django.shortcuts import render

# Create your views here.


def create_request(request):
    return render(request, 'requests/request-create.html')


def delete_request(request, pk):
    return render(request, 'requests/request-delete.html')


def details_request(request, pk):
    return render(request, 'requests/request-details.html')


def edit_request(request, pk):
    return render(request, 'requests/request-edit.html')


def list_request(request):
    return render(request, 'requests/request-list.html')