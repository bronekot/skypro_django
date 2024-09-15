from django.urls import path
from catalog.apps import CatalogConfig
from .views import (
    HomeView,
    ContactsView,
    ProductDetailView,
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("blog/", BlogPostListView.as_view(), name="blogpost_list"),
    path("blog/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("blog/create/", BlogPostCreateView.as_view(), name="blogpost_create"),
    path("blog/<int:pk>/update/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("blog/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blogpost_delete"),
]
