from django.urls import path

from catalog.apps import CatalogConfig

from .views import (
    BlogPostCreateView,
    BlogPostDeleteView,
    BlogPostDetailView,
    BlogPostListView,
    BlogPostUpdateView,
    ContactsView,
    HomeView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductUpdateView,
    VersionCreateView,
    VersionUpdateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blog/", BlogPostListView.as_view(), name="blogpost_list"),
    path("blog/<int:pk>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
    path("blog/<int:pk>/delete/", BlogPostDeleteView.as_view(), name="blogpost_delete"),
    path("blog/<int:pk>/update/", BlogPostUpdateView.as_view(), name="blogpost_update"),
    path("blog/create/", BlogPostCreateView.as_view(), name="blogpost_create"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("version/<int:pk>/update/", VersionUpdateView.as_view(), name="version_update"),
    path("version/create/", VersionCreateView.as_view(), name="version_create"),
]
