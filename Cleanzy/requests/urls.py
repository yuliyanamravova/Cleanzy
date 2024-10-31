from django.urls import path, include

from Cleanzy.requests import views

urlpatterns = [
    path('', views.list_request, name='list-request'),
    path('add/', views.create_request, name='create-request'),
    path('<int:pk>/', include([
        path('delete/', views.delete_request, name='delete-request'),
        path('details/', views.details_request, name='details-request'),
        path('edit/', views.edit_request, name='edit-request'),
    ]))
]