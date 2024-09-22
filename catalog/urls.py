from django.urls import path

from catalog.apps import CatalogConfig

from .views import (
    ContactsView,
    HomeView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductUpdateView,
    VersionCreateView,
    VersionUpdateView,
    CategoryListView,
    ProductListView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("version/<int:pk>/update/", VersionUpdateView.as_view(), name="version_update"),
    path("version/create/", VersionCreateView.as_view(), name="version_create"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("products/", ProductListView.as_view(), name="product_list"),
]
