from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.HomePage, name='Home'),
    path('shop/', views.ShopPage, name='Shop'),
    path('about/', views.AboutPage, name='About'),
    path('contact/', views.ContactPage, name='Contact'),
    path('new-arrivals/', views.NewArrivalsPage, name='NewArrivals'),
    path('catalogue/', views.CataloguePage, name='Catalogue'),
    path('details/<int:id>/', views.DetailsPage, name='Details'),
    path('search/', views.search, name='Search'),
    path('sort-desc/', views.sort_desc, name='sort-desc'),
    path('sort-asc/', views.sort_asc, name='sort-asc'),
    path('sort-l-to-h/', views.sort_l_to_h, name='sort-l-to-h'),
    path('sort-h-to-l/', views.sort_h_to_l, name='sort-h-to-l'),
    path('filter-lr/', views.filter_LR, name='filter-lr'),
    path('filter-br/', views.filter_BR, name='filter-br'),
    path('filter-k/', views.filter_K, name='filter-k'),
]