from django.contrib import admin

from blog.models import BlogPost

# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "content")
    actions = ["make_published", "make_unpublished"]

    def make_published(self, request, queryset):
        queryset.update(is_published=True)

    make_published.short_description = "Опубликовать выбранные статьи"

    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)

    make_unpublished.short_description = "Снять с публикации выбранные статьи"
    make_unpublished.short_description = "Снять с публикации выбранные статьи"
