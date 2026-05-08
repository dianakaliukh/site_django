from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Основні сторінки
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # Кошик
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # Відгуки та Розсилка
    path('product/<int:product_id>/review/', views.add_review, name='add_review'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),

    # === АУТЕНТИФІКАЦІЯ (Лабораторна 8) ===

    # Стандартні шляхи Django (login, logout, password_reset тощо)
    path('accounts/', include('django.contrib.auth.urls')),

    # Реєстрація та Профіль
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Кастомний вихід (у нових версіях Django рекомендується через POST,
    # але ми додамо явний шлях, якщо знадобиться)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]