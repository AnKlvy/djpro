from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', PagesHome.as_view(), name='home'),
    path('product/<slug:prod_slug>/', ShowProduct.as_view(), name='product'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('category/<slug:cat_slug>/', ProdCategory.as_view(), name='category')

]
