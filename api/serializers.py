from rest_framework import serializers
from main.models import Stock, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']
        read_only_fields = ['create_date', 'last_mod']


class StockSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        read_only_fields = ['create_date', 'last_mod']
        model = Stock
        fields = '__all__'
        depth = 2
