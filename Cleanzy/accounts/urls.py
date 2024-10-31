from django.urls import path, include

from Cleanzy.accounts import views

urlpatterns = [
    path('register/', views.create_account, name='create-account'),
    path('log-in', views.log_in_account, name='log-in-account'),
    path('<int:pk>/', include([
        path('delete/', views.delete_account, name='delete-account'),
        path('details/', views.details_account, name='details-account'),
        path('edit/', views.edit_account, name='edit-account'),
        path('log-out', views.log_out_account, name='log-out-account'),
    ]))
]