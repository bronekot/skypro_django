from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ProductForm, VersionForm
from .models import BlogPost, Product, Version


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_version"] = self.object.get_active_version()
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно создан.")
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        messages.success(self.request, "Продукт успешно обновлен.")
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:home")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Продукт успешно удален.")
        return super().delete(request, *args, **kwargs)


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        messages.success(self.request, "Версия успешно создана.")
        return super().form_valid(form)


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        messages.success(self.request, "Версия успешно обновлена.")
        return super().form_valid(form)


# Оставляем существующие представления для BlogPost без изменений
class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blogpost_list.html"
    context_object_name = "blogposts"

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blogpost_detail.html"
    context_object_name = "blogpost"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.view_count += 1
        obj.save()
        return obj


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blogpost_form.html"
    fields = ["title", "content", "preview_image", "is_published"]
    success_url = reverse_lazy("catalog:blogpost_list")


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blogpost_form.html"
    fields = ["title", "slug", "content", "preview_image", "is_published"]

    def get_success_url(self):
        return reverse_lazy("catalog:blogpost_detail", args=[self.object.pk])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blogpost_confirm_delete.html"
    success_url = reverse_lazy("catalog:blogpost_list")
    success_url = reverse_lazy("catalog:blogpost_list")


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blogpost_confirm_delete.html"
    success_url = reverse_lazy("catalog:blogpost_list")
    success_url = reverse_lazy("catalog:blogpost_list")
