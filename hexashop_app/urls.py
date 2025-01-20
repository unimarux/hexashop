from .views import  HomeView , ProductsView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/category/<slug:slug>/', ProductsView.as_view(),name='products')
]