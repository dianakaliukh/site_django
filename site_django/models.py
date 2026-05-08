from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User  # Імпортуємо стандартну модель користувача


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

    is_popular = models.BooleanField(default=False, verbose_name="Популярний товар (на головну)")
    is_active = models.BooleanField(default=True, verbose_name="Активний (відображати на сайті)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"


# ОНОВЛЕНА МОДЕЛЬ ЗАМОВЛЕННЯ (Лабораторна 8)
class Order(models.Model):
    # Прив'язуємо замовлення до користувача
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Клієнт")
    # Додаємо можливість зберігати кілька товарів у текстовому вигляді (або один основний)
    # Для простоти лаби залишимо зв'язок з одним продуктом, але додамо суму
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Товар")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Загальна вартість")

    # Статус замовлення
    is_completed = models.BooleanField(default=False, verbose_name="Виконано")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Замовлення №{self.id} від {self.user.username}"

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ['-created_at']


# Оцінка товару
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


# Підписка на розсилку
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email для розсилки")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата підписки")

    class Meta:
        verbose_name = "Підписка на розсилку"
        verbose_name_plural = "Підписки на розсилку"

    def __str__(self):
        return self.email