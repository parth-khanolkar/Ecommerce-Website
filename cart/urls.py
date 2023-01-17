from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartPage, name='Cart'),
    path('add_cart/<int:id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:id>/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.CheckoutPage, name='Checkout'),
    path('thankyou/', views.ThankyouPage, name='Thankyou'),
]