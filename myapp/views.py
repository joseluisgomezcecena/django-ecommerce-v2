from django.shortcuts import render
from .models import Product


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')


def products(request):
    product_list = Product.objects.all()
    return render(request, 'myapp/products.html', {'products': product_list})
