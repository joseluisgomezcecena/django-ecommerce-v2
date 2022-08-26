from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')


def products(request):
    product_list = Product.objects.all()
    return render(request, 'myapp/products.html', {'products': product_list})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'myapp/product_detail.html', {'product': product})
