from .views import HomeView, ProductsView, ProductDetailView, CartView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/category/<slug:slug>/', ProductsView.as_view(),name='products'),
    path('products/product/<slug:slug>/', ProductDetailView.as_view(),name='product'),
    path('cart/<slug:slug>', CartView.as_view(),name='cart'),
]