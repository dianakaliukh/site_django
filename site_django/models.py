from django.db import models

# Категорія (Кільця, Сережки, Браслети тощо)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    # Додаємо фото для плитки категорій у каталозі
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
    # Використовуємо DecimalField для грошей — це професійний стандарт
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    # Додаємо фото товару для сторінки товарів
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Зображення товару")
    # Зв'язок з категорією
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Категорія")
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