from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
# видео классы представлений чтобы отображать категории
class PagesHome(ListView):
    model = Products
    template_name = 'pages/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Products.objects.filter(is_published=True)


# def home_screen_view(request):
#     print(request.headers)
#     products = Products.objects.order_by('-time_create')
#     return render(request, 'pages/index.html', {'products': products})

class ShowProduct(DetailView):
    model = Products
    template_name = 'pages/product.html'
    slug_url_kwarg = 'prod_slug'
    context_object_name = 'product'


# def show_product(request, prod_slug):
#     product = get_object_or_404(Products, slug=prod_slug)
#     return render(request, 'pages/product.html', {'product': product})

class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'pages/addpost.html'
    # success_url = reverse_lazy('home')


# def add_post(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # try:
#                 # Posts.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#             # except:
#             #     form.add_error(None, 'Error of adding post')
#     else:
#         form = AddPostForm()
#     return render(request, 'pages/addpost.html',
#                   {'form': form, 'title': 'Adding post'})


# ERRORS LOGIC
def error_404(request, exception):
    return render(request, 'errors/404.html')


def error500(request, *args, **argv):
    return render(request, '500.html')


def error_403(request, exception):
    return render(request, '403.html')


def error_400(request, exception):
    return render(request, '400.html', data)
