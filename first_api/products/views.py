from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Product, Manufacturer

def product_list(request):
    products = Product.objects.all()
    data = {"products": list(products.values())}
    return JsonResponse(data)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = {
        "name": product.name,
        "manufacturer": product.manufacturer.name,
        "description": product.description,
        "photo": product.photo.url,
        "price": product.price,
        "shipping_cost": product.shipping_cost,
        "quantity": product.quantity
    }
    return JsonResponse(data)

def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    data = {"manufacturers": list(manufacturers.values())}
    return JsonResponse(data)

def manufacturer_detail(request, pk):
    manufacturer = get_object_or_404(Manufacturer, pk=pk)
    data = {
        "name": manufacturer.name,
        "location": manufacturer.location,
        "active": manufacturer.active,
    }
    return JsonResponse(data)