from django.urls import path, include

from Cleanzy.warehouses import views
urlpatterns = [
    path('add/', views.AddWarehouseView.as_view(), name='add-warehouse'),
    path('<int:pk>', include([
        path('edit/', views.EditWarehouseView.as_view(), name='edit-warehouse'),
        path('delete/', views.DeleteWarehouseView.as_view(), name='delete-warehouse'),
        path('details/', views.DetailsWarehouseView.as_view(), name='detail-warehouse')
    ]))

]