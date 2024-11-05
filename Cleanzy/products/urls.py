from django.urls import path, include

from Cleanzy.products import views

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('add/', views.CreateProductView.as_view(), name='create-product'),
    path('<int:pk>/', include([
        path('delete/', views.DeleteProductView.as_view(), name='delete-product'),
        path('details/', views.DetailProductView.as_view(), name='details-product'),
        path('edit/', views.EditProductView.as_view(), name='edit-product'),
    ]))
]