from .models import Product, Category
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def catalog(request):
    categories = Category.objects.all()
    return render(request, 'catalog.html', {"categories": categories})

def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'products.html', {"products": products})

def contacts(request):
    return render(request, 'contacts.html')