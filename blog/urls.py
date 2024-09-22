from django.urls import path

from blog.apps import BlogConfig

from .views import (
    BlogPostCreateView,
    BlogPostDeleteView,
    BlogPostDetailView,
    BlogPostListView,
    BlogPostUpdateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", BlogPostListView.as_view(), name="blogpost_list"),
    path("blog/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("blog/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blogpost_delete"),
    path("blog/<int:pk>/update/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("blog/create/", BlogPostCreateView.as_view(), name="blogpost_create"),
]
