from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'stock', views.StockViewSet, basename='stocks')
router.register(r'product', views.ProductViewSet, basename='products')
router.register(r'stockFromProduct', views.StockFromProductViewSet,
                basename='stock_from_product')


urlpatterns = [
    path('', include(router.urls)),
    path('loadProduct/<key>/', views.loadProductsAPIView.as_view()),
    path('searchProduct/', views.searchProduct.as_view())
]
