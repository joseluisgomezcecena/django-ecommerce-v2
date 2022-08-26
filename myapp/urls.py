from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]
