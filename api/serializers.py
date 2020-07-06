from rest_framework import serializers
from main.models import (Stock, Product, CheckIn, CheckOut, Shift,
                         Category, Recipt)
from django.contrib.auth.models import User
from datetime import date, datetime
from django.utils.timezone import get_current_timezone


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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'is_staff', 'first_name', 'last_name']
        read_only_fields = ['username', 'is_staff']


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'

    def create(self, validated_data):
        # If shift exists
        if Shift.objects.filter(
                user=self.context['request'].user,
                date=datetime.now(tz=get_current_timezone())).exists():
            # If Check In Exists
            if Shift.objects.filter(
                    user=self.context['request'].user,
                    date=datetime.now(tz=get_current_timezone()))[0].check_in:
                raise serializers.ValidationError('Check-in Already Exists')
            else:
                shift_obj = Shift.objects.get_or_create(
                    user=self.context['request'].user,
                    date=datetime.now(tz=get_current_timezone()))[0]

                obj = CheckIn.objects.create(
                    user=self.context['request'].user,
                    date=datetime.now(tz=get_current_timezone()))
                obj.save()
                shift_obj.check_in = obj
                shift_obj.save()
                return obj
        # If shift not exists
        else:
            # Create Shift
            shift_obj = Shift.objects.get_or_create(
                user=self.context['request'].user,
                date=datetime.now(tz=get_current_timezone()))[0]

            # Create Check-In
            obj = CheckIn.objects.create(
                user=self.context['request'].user,
                date=datetime.now(tz=get_current_timezone()))
            obj.save()
            shift_obj.check_in = obj
            shift_obj.save()
            return obj


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = '__all__'

    def create(self, validated_data):
        # If shift exists
        if Shift.objects.filter(
                user=self.context['request'].user,
                date=datetime.now(tz=get_current_timezone())).exists():

            shift_obj = Shift.objects.get(
                user=self.context['request'].user,
                date=datetime.now(tz=get_current_timezone()))

            # If Check Out Exists,
            if shift_obj.check_out:
                raise serializers.ValidationError('Check-out Already Exists')

            # If not check-in exists in shift
            if not shift_obj.check_in:
                raise serializers.ValidationError(
                    'You need to check-in first.')
            else:
                shift_obj = Shift.objects.get_or_create(
                    user=self.context['request'].user,
                    date=datetime.now(tz=get_current_timezone()))[0]

                obj = CheckOut.objects.create(
                    user=self.context['request'].user,
                    date=datetime.now(tz=get_current_timezone()))
                obj.save()
                shift_obj.check_out = obj
                shift_obj.save()
                return obj

        # If shift not exists
        else:
            # Create Shift
            shift_obj = Shift.objects.get_or_create(
                user=self.context['request'].user,
                date=datetime.now(tz=get_current_timezone()))[0]

            # If check-in exists in shift
            if not shift_obj.check_in:
                raise serializers.ValidationError(
                    'You need to check-in first.')
            # If not check-in exists in shift
            else:
                obj = CheckOut.objects.create(
                    user=self.context['request'].user,
                    date=datetime.now(tz=get_current_timezone()))
                obj.save()
                shift_obj.check_out = obj
                shift_obj.save()
                return obj


class ShiftSerializer(serializers.ModelSerializer):
    check_in = serializers.SlugRelatedField(slug_field='date', read_only=True)
    check_out = serializers.SlugRelatedField(slug_field='date', read_only=True)

    class Meta:
        model = Shift
        fields = '__all__'


class AllShiftSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    check_in = serializers.SlugRelatedField(slug_field='date', read_only=True)
    check_out = serializers.SlugRelatedField(slug_field='date', read_only=True)

    class Meta:
        model = Shift
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


class ReciptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipt
        fields = '__all__'
