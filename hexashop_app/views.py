from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views.generic import View , DeleteView , DetailView , ListView , UpdateView , CreateView
from hexashop_app.models import Product , Category , Type

# Create your views here.

class HomeView(ListView):
    queryset = Product.objects.all().order_by('-id')[:6]
    template_name = 'index.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['types'] = Type.objects.all()
        return context


class ProductsView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Product.objects.filter(category__slug=slug).order_by('-id')
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['types'] = Type.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'single-product.html'
    context_object_name = 'product'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Product.objects.filter(slug=slug)

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['types'] = Type.objects.all()
        return context


class CartView(View):
    def get(self , request:WSGIRequest , slug:str):
        page = request.META.get("HTTP_REFERER" , 'home')
        return redirect('home')

