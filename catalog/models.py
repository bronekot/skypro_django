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
    image = models.ImageField(
        upload_to="products/", verbose_name="Изображение", null=True, blank=True
    )
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, verbose_name="Категория"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


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
