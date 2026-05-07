from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Категорія (Кільця, Сережки, Браслети тощо)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    image = models.ImageField(upload_to='categories/', null=True, blank=True, verbose_name="Зображення категорії")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


# Продукт (Ювелірні вироби LuxeCharm)
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва товару")
    description = models.TextField(null=True, blank=True, verbose_name="Опис товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Зображення товару")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категорія")

    # НОВІ ПОЛЯ
    is_popular = models.BooleanField(default=False, verbose_name="Популярний товар (на головну)")
    is_active = models.BooleanField(default=True, verbose_name="Активний (відображати на сайті)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"


# Замовлення
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    customer_name = models.CharField(max_length=100, verbose_name="Ім'я клієнта")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Замовлення: {self.customer_name} ({self.product.name})"

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"


# НОВА МОДЕЛЬ: Оцінка товару (Лабораторна 7)
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name="Товар")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Оцінка (1-5)"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата оцінки")

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
        ordering = ['-created_at']


# НОВА МОДЕЛЬ: Підписка на розсилку (Лабораторна 7)
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email для розсилки")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата підписки")

    class Meta:
        verbose_name = "Підписка на розсилку"
        verbose_name_plural = "Підписки на розсилку"

    def __str__(self):
        return self.email