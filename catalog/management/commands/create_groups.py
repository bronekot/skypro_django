from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создать группы"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Модератор")
        if created:
            self.stdout.write(self.style.SUCCESS("Группа 'Модератор' создана"))
        else:
            self.stdout.write(self.style.SUCCESS("Группа 'Модератор' уже существует"))

        permissions = [
            "can_unpublish_product",
            "can_change_product_description",
            "can_change_product_category",
        ]

        for permission in permissions:
            perm = Permission.objects.get(codename=permission)
            group.permissions.add(perm)
            self.stdout.write(self.style.SUCCESS(f"Право '{permission}' добавлено к группе 'Модератор'"))
