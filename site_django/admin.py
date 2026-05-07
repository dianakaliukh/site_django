from django.contrib import admin
from .models import Category, Product, Order

# Налаштування заголовків адмінки (опціонально, для стилю)
admin.site.site_header = "LuxeCharm Administration"
admin.site.site_title = "LuxeCharm Ювелірні вироби"
admin.site.index_title = "Панель керування магазином"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)  # Пошук по назві категорії
    list_filter = ('created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Додаємо is_popular та is_active у список
    list_display = ('name', 'price', 'category', 'is_popular', 'is_active', 'created_at')

    # Дозволяємо редагувати популярність та активність прямо зі списку (дуже зручно!)
    list_editable = ('is_popular', 'is_active', 'price')

    # Фільтри збоку для швидкого сортування
    list_filter = ('category', 'is_popular', 'is_active', 'created_at')

    # Пошук по назві та опису
    search_fields = ('name', 'description')

    # Автоматичне групування полів у формі редагування
    fields = ('name', 'category', 'price', 'description', 'image', ('is_popular', 'is_active'))


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product', 'created_at')
    list_filter = ('created_at', 'product')
    search_fields = ('customer_name', 'product__name')
    readonly_fields = ('created_at',)  # Замовлення краще не редагувати вручну