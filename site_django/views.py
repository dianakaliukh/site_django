from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# Головна сторінка
def home(request):
    return render(request, 'home.html')


# Сторінка каталогу (всі категорії)
def catalog(request):
    categories = Category.objects.all()
    return render(request, 'catalog.html', {"categories": categories})


# Сторінка товарів конкретної категорії
def products_by_category(request, category_id):
    # Використовуємо get_object_or_404, щоб якщо категорії не існує, вибило помилку 404, а не збій сервера
    category = get_object_or_404(Category, id=category_id)

    # Отримуємо товари саме цієї категорії
    products = Product.objects.filter(category=category)

    return render(request, 'products.html', {
        "category": category,
        "products": products
    })


# Контакти
def contacts(request):
    return render(request, 'contacts.html')

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, pk):
    # Шукаємо товар, або видаємо 404, якщо не знайшли
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})