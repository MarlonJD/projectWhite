from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken import views as rest_views
from . import views

router = routers.DefaultRouter()
router.register(r'stock', views.StockViewSet, basename='stocks')
router.register(r'product', views.ProductViewSet, basename='products')
router.register(r'stockFromProduct',
                views.StockFromProductViewSet,
                basename='stock_from_product')
router.register(r'checkIn', views.CheckInViewSet, basename='checkIn')
router.register(r'checkOut', views.CheckOutViewSet, basename='checkOut')
router.register(r'shift', views.ShiftViewSet, basename='shift')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/',
         rest_views.obtain_auth_token,
         name='api-token-auth'),
    path('loadProduct/<key>/', views.loadProductsAPIView.as_view()),
    path('searchProduct/', views.searchProduct.as_view()),
    path('getUserDetail/', views.UserDetailsAPIView.as_view()),
]
