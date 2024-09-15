import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load data from JSON file and populate the database"

    @staticmethod
    def json_read_categories():
        with open("catalog/fixtures/base.json", encoding="utf-8") as f:
            data = json.load(f)
            return [item for item in data if item["model"] == "catalog.category"]

    @staticmethod
    def json_read_products():
        with open("catalog/fixtures/base.json", encoding="utf-8") as f:
            data = json.load(f)
            return [item for item in data if item["model"] == "catalog.product"]

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        category_for_create = []
        product_for_create = []

        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for item in Command.json_read_categories():
            fields = item["fields"]
            category_for_create.append(Category(id=item["pk"], name=fields["name"]))

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for item in Command.json_read_products():
            fields = item["fields"]
            product_for_create.append(
                Product(
                    id=item["pk"],
                    name=fields["name"],
                    description=fields["description"],
                    image=fields["image"],
                    category=Category.objects.get(pk=fields["category"]),
                    price=fields["price"],
                    created_at=fields["created_at"],
                    updated_at=fields["updated_at"],
                )
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)

        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))
