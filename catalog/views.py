import re
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy
from .models import Product, BlogPost


class HomeView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "object_list"


class ContactsView(View):
    def get(self, request):
        return render(request, "contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, phone, message)
        return render(request, "contacts.html")


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "object"


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blogpost_list.html"
    context_object_name = "blogposts"

    def get_queryset(self):
        # Фильтруем статьи, чтобы отображать только опубликованные
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blogpost_detail.html"
    context_object_name = "blogpost"

    def get_object(self, queryset=None):
        # Получаем объект статьи и увеличиваем счетчик просмотров
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj


def generate_slug(text):
    # Приводим текст к нижнему регистру
    text = text.lower()
    # Заменяем пробелы на дефисы
    text = re.sub(r"\s+", "-", text)
    # Удаляем все небезопасные символы
    text = re.sub(r"[^a-z0-9\-]", "", text)
    # Удаляем начальные и конечные дефисы
    text = text.strip("-")
    return text


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blogpost_form.html"
    fields = ["title", "content", "preview_image", "is_published"]
    success_url = reverse_lazy("catalog:blogpost_list")

    def form_valid(self, form):
        form.instance.slug = generate_slug(form.instance.title)
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blogpost_form.html"
    fields = ["title", "slug", "content", "preview_image", "is_published"]

    def get_success_url(self):
        return reverse("catalog:blogpost_detail", args=[self.object.pk])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blogpost_confirm_delete.html"
    success_url = reverse_lazy("catalog:blogpost_list")
