from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page

from .views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
# router.register(r'products', ProductsApiList)
# router.register(r'products/<int:pk>/', ProductsAPIUpdate)
# router.register(r'productdelete/<int:pk>/', ProductsAPIDestroy)


urlpatterns = [
    # path('', cache_page(60)(PagesHome.as_view()), name='home'),
    path('', PagesHome.as_view(), name='home'),
    path('api/v1/', include(router.urls)),
    # path('api/v1/products/', ProductsApiList.as_view()),
    # path('api/v1/products/<int:pk>/', ProductsAPIUpdate.as_view()),
    # path('api/v1/productsdelete/<int:pk>/', ProductsAPIDestroy.as_view()),
    # path('api/v1/products/', ProductViewSet.as_view({'get': 'list'})),
    # path('api/v1/products/<int:pk>/', ProductViewSet.as_view({'put': 'update'})),
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
