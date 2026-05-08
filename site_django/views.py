from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  # Для реєстрації
from django.contrib.auth.decorators import login_required  # Для захисту профілю
from .models import Product, Category, Review, NewsletterSubscription, Order


# === ГОЛОВНА СТОРІНКА ===
def home(request):
    popular_products = Product.objects.filter(is_popular=True, is_active=True)[:4]
    return render(request, 'home.html', {
        'popular_products': popular_products
    })


# === КАТАЛОГ ===
def catalog(request):
    categories = Category.objects.all()
    return render(request, 'catalog.html', {"categories": categories})


# === ТОВАРИ В КАТЕГОРІЇ ===
def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_active=True)
    return render(request, 'products.html', {
        "category": category,
        "products": products
    })


# === ДЕТАЛІ ТОВАРУ (З ОЦІНКАМИ) ===
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # Розрахунок середнього балу
    average_rating = product.reviews.aggregate(Avg('rating'))['rating__avg']
    if average_rating:
        average_rating = round(average_rating, 1)
    else:
        average_rating = 0

    return render(request, 'product_detail.html', {
        'product': product,
        'average_rating': average_rating
    })


# === ДОДАВАННЯ ВІДГУКУ (ОЦІНКИ) ===
def add_review(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        rating = request.POST.get('rating')
        if rating:
            Review.objects.create(product=product, rating=rating)
            messages.success(request, "Дякуємо за вашу оцінку!")
    return redirect('product_detail', pk=product_id)


# === ПІДПИСКА НА РОЗСИЛКУ ===
def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not NewsletterSubscription.objects.filter(email=email).exists():
                NewsletterSubscription.objects.create(email=email)
                messages.success(request, "Ви успішно підписалися на розсилку LuxeCharm!")
            else:
                messages.info(request, "Цей Email вже підписаний.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))


# === КОШИК (CART) ===

def cart_add(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    request.session['cart'] = cart
    messages.success(request, "Товар додано до кошика")
    return redirect('cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        # Додана обробка помилки, якщо товар був видалений з БД, але лишився в сесії
        try:
            product = Product.objects.get(id=product_id)
            item_total = product.price * quantity
            total_price += item_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total': item_total
            })
        except Product.DoesNotExist:
            continue

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def cart_remove(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        messages.success(request, "Товар видалено з кошика")

    return redirect('cart_detail')


# === АУТЕНТИФІКАЦІЯ ТА ПРОФІЛЬ (Лабораторна 8) ===

# Реєстрація
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Акаунт створено! Тепер ви можете увійти.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Особистий кабінет
@login_required
def profile(request):
    if request.user.is_staff:
        # Адмін бачить замовлення всіх користувачів
        orders = Order.objects.all().order_by('-created_at')
    else:
        # Звичайний юзер бачить тільки свої
        orders = Order.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'profile.html', {
        'orders': orders
    })


# === КОНТАКТИ ===
def contacts(request):
    return render(request, 'contacts.html')