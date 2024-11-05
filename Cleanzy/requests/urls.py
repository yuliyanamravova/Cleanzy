from django.urls import path, include

from Cleanzy.requests import views

urlpatterns = [
    path('', views.list_request, name='list-request'),
    path('add/', views.CreateRequestView.as_view(), name='create-request'),
    path('<int:id>/', include([
        path('delete/', views.DeleteRequestView.as_view(), name='delete-request'),
        path('details/', views.DetailRequestView.as_view(), name='details-request'),
        path('edit/', views.EditRequestView.as_view(), name='edit-request'),
    ]))
]