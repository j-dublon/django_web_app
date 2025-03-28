from django.contrib import admin
from django.urls import path
from . import views

app_name="first_app"
urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('products/<int:id>/', views.product_detail, name="product_detail")
]