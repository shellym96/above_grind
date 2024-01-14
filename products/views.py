from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all of the products - sorting and searching """

    products = Product.objects.all()
    print(products)

    context = {
        'products': products,
    }
    return render(request, 'products/products.html',context)


def product_detail(request, product_id):
    """ A view to show indiviual products details """

    product = get_object_or_404(Product, pk-product_id)

    context = {
        'products': products,
    }
    return render(request, 'products/product_detail.html')