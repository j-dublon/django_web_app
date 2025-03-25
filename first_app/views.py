from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World")

def products(request):
    products = ["Iphone", "Mac", "IPad"]
    return HttpResponse(products)
