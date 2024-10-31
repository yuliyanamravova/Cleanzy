from django.urls import path, include

from Cleanzy.products import views

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('add/', views.create_product, name='create-product'),
    path('<int:pk>/', include([
        path('delete/', views.delete_product, name='delete-product'),
        path('details/', views.details_product, name='details-product'),
        path('edit/', views.edit_product, name='edit-product'),
    ]))
]