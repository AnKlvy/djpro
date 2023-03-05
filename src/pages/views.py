from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home_screen_view(request):
    print(request.headers)
    products = Products.objects.order_by('-time_create')
    return render(request, 'index.html', {'products': products})

def show_product(request, prod_slug):
    product = get_object_or_404(Products, slug = prod_slug)
    return render(request, 'pages/product.html', {'product':product})

# ERRORS LOGIC
def error_404(request, exception):

        return render(request,'errors/404.html')

def error500(request, *args, **argv):
    return render(request, '500.html')
          
def error_403(request, exception):

        return render(request,'403.html')

def error_400(request,  exception):
        return render(request,'400.html', data)