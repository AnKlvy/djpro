from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', PagesHome.as_view(), name='home'),
    path('product/<slug:prod_slug>/', ShowProduct.as_view(), name='product'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('category/<slug:cat_slug>/', ProdCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
]
