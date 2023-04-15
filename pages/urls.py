from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page

from .views import *

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'products', ProductsViewSet)

urlpatterns = [
    # path('', cache_page(60)(PagesHome.as_view()), name='home'),
    path('', PagesHome.as_view(), name='home'),
    # path('api/v1/', include(router.urls)),
    path('api/v1/products/', ProductsViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('product/<slug:prod_slug>/', ShowProduct.as_view(), name='product'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('about/', about, name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('category/<slug:cat_slug>/', ProdCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
]
