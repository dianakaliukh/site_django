from django.contrib import admin
from .models import Category, Product, Order, Review, NewsletterSubscription

# Налаштування заголовків адмінки
admin.site.site_header = "LuxeCharm Administration"
admin.site.site_title = "LuxeCharm Ювелірні вироби"
admin.site.index_title = "Панель керування магазином"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_popular', 'is_active', 'created_at')
    list_editable = ('is_popular', 'is_active', 'price')
    list_filter = ('category', 'is_popular', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    fields = ('name', 'category', 'price', 'description', 'image', ('is_popular', 'is_active'))


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # ВИПРАВЛЕНО: 'customer_name' замінено на 'user'
    list_display = ('id', 'user', 'product', 'total_price', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at', 'product')
    search_fields = ('user__username', 'product__name')
    readonly_fields = ('created_at',)
    list_editable = ('is_completed',) # Дозволяє адміну швидко відмічати виконані замовлення


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(NewsletterSubscription)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at',)