from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    return HttpResponse("Hello World")

def products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'first_app/index.html', context)
