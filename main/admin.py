from django.contrib import admin
from .models import Stock, Product


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    readonly_fields = ['create_date', 'last_mod']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ['create_date', 'last_mod']
