from django.contrib.auth import get_user_model
from django.db import models


class BlogPost(models.Model):
    """
    Представляет блоговую запись.
    Атрибуты:
        title (str): Заголовок записи.
        slug (str): Слаг записи.
        content (str): Содержимое записи.
        preview_image (ImageField): Превью изображение записи.
        created_at (DateTimeField): Дата и время создания записи.
        is_published (bool): Признак публикации записи.
        view_count (int): Количество просмотров записи.
    Методы:
        __str__(): Возвращает строковое представление записи.
    """

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(max_length=255, unique=True, verbose_name="Слаг")
    content = models.TextField(verbose_name="Содержимое")
    preview_image = models.ImageField(
        upload_to="previews/",
        verbose_name="Превью изображение",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    view_count = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-").lower()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
