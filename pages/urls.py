from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *

from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'products', ProductViewSet)
# router.register(r'products', ProductsApiList)
# router.register(r'products/<int:pk>/', ProductsAPIUpdate)
# router.register(r'productdelete/<int:pk>/', ProductsAPIDestroy)


urlpatterns = [
    # path('', cache_page(60)(PagesHome.as_view()), name='home'),
    path('', PagesHome.as_view(), name='home'),
    # path('api/v1/', include(router.urls)),
    path('api/v1/products/', ProductsApiList.as_view()),
    path('api/v1/products/<int:pk>/', ProductsAPIUpdate.as_view()),
    path('api/v1/productsdelete/<int:pk>/', ProductsAPIDestroy.as_view()),
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
    path('cart/', cart_view, name='cart'),

    path('api/v1/drf-auth/', include('rest_framework.urls')),

    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    #Add to cards Afunctions
    path('product/add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('product/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

]

