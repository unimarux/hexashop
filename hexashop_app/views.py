from django.shortcuts import render
from django.views.generic import View , DeleteView , DetailView , ListView , UpdateView , CreateView
from hexashop_app.models import Product


# Create your views here.

class HomeView(ListView):
    model = Product
    template_name = 'index.html'