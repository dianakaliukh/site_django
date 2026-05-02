from django.urls import path
from . import views
urlpatterns = [
    # Додаємо імена для кожного маршруту
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<int:category_id>/', views.products_by_category, name='products_by_category'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]