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


def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['upload']
        Product.objects.create(name=name, description=description, price=price, image=image)
        # product = Product(name=name, description=description, price=price, image=image)
        # product.save()
        return render(request, 'myapp/add_product.html')
    else:
        return render(request, 'myapp/add_product.html')
