"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import (
    # home_screen_view,
    # show_product,
    # add_post,
    AddPost,
    PagesHome,
    ShowProduct
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PagesHome.as_view(), name='home'),
    path('product/<slug:prod_slug>/', ShowProduct.as_view(), name='product'),
    path('addpost/', AddPost.as_view(), name='addpost'),

]
handler500 = 'pages.views.error500'
handler404 = 'pages.views.error_404'
handler403 = 'pages.views.error_403'
handler400 = 'pages.views.error_400'
