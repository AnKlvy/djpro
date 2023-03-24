from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .utils import *


# Create your views here.
# видео классы представлений чтобы отображать категории
class PagesHome(DataMixin, ListView):
    model = Products
    template_name = 'pages/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Products.objects.filter(is_published=True).prefetch_related('categories')

    # def home_screen_view(request):
    #     print(request.headers)
    #     products = Products.objects.order_by('-time_create')
    #     return render(request, 'pages/index.html', {'products': products})


class ShowProduct(DataMixin, DetailView):
    model = Products
    template_name = 'pages/product.html'
    slug_url_kwarg = 'prod_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_product(request, prod_slug):
#     product = get_object_or_404(Products, slug=prod_slug)
#     return render(request, 'pages/product.html', {'product': product})

class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'pages/addpost.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    # login_url = reverse_lazy('home')
    # raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add post")
        return dict(list(context.items()) + list(c_def.items()))


class ProdCategory(DataMixin, ListView):
    model = Products
    template_name = 'pages/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Products.objects.filter(categories__slug=self.kwargs['cat_slug'], is_published=True).prefetch_related(
            'categories')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = ProdCategories.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title="Category - " + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

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


# @login_required
def about(request):
    return render(request, 'pages/about.html', {'menu': menu, 'title': 'About'})


def login(request):
    return render(request, 'pages/login.html')


def contact(request):
    return render(request, 'pages/contact.html')


# ERRORS LOGIC
def error_404(request, exception):
    return render(request, 'errors/404.html')


def error500(request, *args):
    return render(request, 'errors/500.html')


def error_403(request, exception):
    return render(request, 'errors/403.html')


def error_400(request, exception):
    return render(request, 'errors/400.html')
