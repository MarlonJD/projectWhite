from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.StockListView.as_view(), name='index'),
    path('stocks/<page>/', views.StockListView.as_view(), name="index-page"),
    path('recipt/list/', views.ReciptListView.as_view(), name='recipt-list'),
    path('recipt/list/<page>/',
         views.ReciptListView.as_view(),
         name="recipt-list-page"),
    path('stock/add/', views.StockAddPage.as_view(), name='stock-add'),
    path('stock/remove', views.StockRemovePage.as_view(), name='stock-remove'),
    path('recipt/add/', views.ReciptCreate.as_view(), name='add-recipt'),
    path('recipt/success/',
         views.ReciptSuccess.as_view(),
         name='success-recipt'),
    path('shifts/', views.ShiftAPIView.as_view(), name="shift-list")
]
