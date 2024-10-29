from django.urls import path

from Cleanzy.common import views

urlpatterns = [
    path('', views.home, name='home')
]