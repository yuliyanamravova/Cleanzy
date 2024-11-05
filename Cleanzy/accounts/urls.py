from django.urls import path, include

from Cleanzy.accounts import views

urlpatterns = [
    path('register/', views.CreateAccountView.as_view(), name='create-account'),
    path('log-in', views.log_in_account, name='log-in-account'),
    path('<int:id>/', include([
        path('delete/', views.DeleteAccountView.as_view(), name='delete-account'),
        path('details/', views.details_account, name='details-account'),
        path('edit/', views.EditAccountView.as_view(), name='edit-account'),
        path('log-out', views.log_out_account, name='log-out-account'),
    ]))
]