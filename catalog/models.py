from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    """
    Представляет продукт в каталоге.
    Атрибуты:
        name (str): Название продукта.
        description (str): Описание продукта.
        image (ImageField): Изображение продукта.
        category (ForeignKey): Категория продукта.
        price (DecimalField): Цена продукта.
        created_at (DateTimeField): Дата и время создания продукта.
        updated_at (DateTimeField): Дата и время последнего обновления продукта.
    Методы:
        __str__(): Возвращает строковое представление продукта.
    """

    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="products/", verbose_name="Изображение", null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self):
        return str(self.name)

    def get_active_version(self):
        return self.versions.filter(is_current=True).first()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта"),
            ("can_change_product_description", "Может менять описание любого продукта"),
            ("can_change_product_category", "Может менять категорию любого продукта"),
        ]


class Category(models.Model):
    """
    Представляет категорию в каталоге.
    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        created_at (DateTimeField): Дата и время создания категории.
        updated_at (DateTimeField): Дата и время последнего обновления категории.
    Методы:
        __str__(): Возвращает строковое представление категории.
    """

    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="versions")
    version_number = models.CharField(max_length=50, verbose_name="Номер версии")
    version_name = models.CharField(max_length=255, verbose_name="Название версии")
    is_current = models.BooleanField(default=False, verbose_name="Текущая версия")

    def __str__(self):
        return f"{self.product.name} - {self.version_name}"

    def save(self, *args, **kwargs):
        if self.is_current:
            Version.objects.filter(product=self.product).exclude(pk=self.pk).update(is_current=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
