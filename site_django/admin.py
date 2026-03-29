from django.contrib import admin
from .models import Category, Product, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at', 'updated_at')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product', 'created_at', 'updated_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)