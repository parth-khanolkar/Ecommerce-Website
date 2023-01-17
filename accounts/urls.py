from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('accounts/login', views.LoginPage, name='Login'),
    path('accounts/logout', views.LogoutPage, name='Logout'),
]