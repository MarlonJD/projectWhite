from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.StockListView.as_view(), name='index'),
    path('stock/add/', views.StockAddPage.as_view(), name='stock-add'),
    path('stock/remove', views.StockRemovePage.as_view(), name='stock-remove'),
    path('stock/<page>/', views.StockListView.as_view(), name="index-page"),
]
