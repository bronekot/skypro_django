from django.core.cache import cache

from .models import Category, Product


def get_categories():
    categories = cache.get("categories")
    if categories is None:
        categories = Category.objects.all()
        cache.set("categories", categories, 60 * 15)  # кешировать на 15 минут
    return categories


def get_products():
    products = cache.get("products")
    if products is None:
        products = Product.objects.all()
        cache.set("products", products, 60 * 15)  # кешировать на 15 минут
    return products
