from django.shortcuts import render
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