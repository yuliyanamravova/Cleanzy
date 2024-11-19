from django.urls import path, include

from Cleanzy.products import views

urlpatterns = [
    path('', views.CatalogueView.as_view(), name='catalogue'),
    path('add/', views.CreateProductView.as_view(), name='create-product'),
    path('<int:pk>/', include([
        path('', views.DetailProductView.as_view(), name='details-product'),
        path('delete/', views.DeleteProductView.as_view(), name='delete-product'),
        path('edit/', views.EditProductView.as_view(), name='edit-product'),
    ]))
]