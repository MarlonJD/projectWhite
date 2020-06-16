from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.StockListView.as_view(), name='index'),
    path('stock/change/', views.StockChangePage.as_view(), name='stock-change'),
    path('stock/<page>/', views.StockListView.as_view(),
         name="index-page"),
]
