from django.contrib import admin
from .models import *


# @admin.register(Stock)
# class StockAdmin(admin.ModelAdmin):
#     readonly_fields = ['create_date', 'last_mod']


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     readonly_fields = ['create_date', 'last_mod']


admin.site.register(Category)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
admin.site.register(Shift)
admin.site.register(Recipt)
