from django.urls import path, include

from Cleanzy.companies import views

urlpatterns = [
    path('add/', views.AddCompanyView.as_view(), name='add-company'),
    path('<int:pk>/', include([
        path('edit/', views.EditCompanyView.as_view(), name='edit-company'),
        path('delete/', views.DeleteCompanyView.as_view(), name='delete-company'),
        path('details/', views.DetailCompanyView.as_view(), name='detail-company')
    ]))
]