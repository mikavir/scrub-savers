from django.shortcuts import render
from products.models import Product
import random


def index(request):
    """ A view to return the index page """
    products = list(Product.objects.all())

    if len(products) > 4:
        products = random.sample(products, 4)

    return render(request, 'home/index.html', {'products': products})
