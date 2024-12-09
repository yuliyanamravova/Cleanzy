from django.contrib.auth.views import LogoutView
from django.urls import path, include

from Cleanzy.accounts import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),

    path('<int:pk>/', include([
        path('', views.DetailsAccountView.as_view(), name='profile-details'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('delete/', views.UserDeleteView.as_view(), name='user-delete')
    ]))
]