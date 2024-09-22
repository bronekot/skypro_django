from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import BlogPost


# Create your views here.
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
    success_url = reverse_lazy("blog:blogpost_list")


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blogpost_form.html"
    fields = ["title", "slug", "content", "preview_image", "is_published"]

    def get_success_url(self):
        return reverse_lazy("blog:blogpost_detail", args=[self.object.pk])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:blogpost_list")
