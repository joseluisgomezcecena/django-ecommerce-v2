from django.shortcuts import render, redirect
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


def update_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.image = request.FILES['upload']
        product.save()
        # return render(request, 'myapp/update_product.html', {'product': product})
        return redirect('myapp:products')
    else:
        return render(request, 'myapp/update_product.html', {'product': product})
