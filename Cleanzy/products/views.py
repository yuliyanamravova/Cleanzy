from django.shortcuts import render


def catalogue(request):
    return render(request, 'products/catalogue.html')

# Create your views here.
def create_product(request):
    return render(request, 'products/product-create.html')


def delete_product(request, pk):
    return render(request, 'products/product-delete.html')


def details_product(request, pk):
    return render(request, 'products/product-details.html')


def edit_product(request, pk):
    return render(request, 'products/product-edit.html')