from django.shortcuts import render

from Cleanzy.companies.models import Company


# Create your views here.
def home(request):
    company = None
    if request.user.is_authenticated:
        company = Company.objects.filter(user=request.user).first()
    return render(request, 'common/home.html', {'company': company})