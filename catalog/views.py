from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    print(f"Products: {products}")
    context = {"object_list": products}
    return render(request, "home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, phone, message)

    return render(request, "contacts.html")


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"object": product}
    return render(request, "product_detail.html", context)
