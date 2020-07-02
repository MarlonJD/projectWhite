# from django.utils.translation import gettext as _
from .permissions import IsAdminUser
# from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .serializers import (StockSerializer, ProductSerializer,
                          UserDetailSerializer, CheckInSerializer,
                          CheckOutSerializer, ShiftSerializer,
                          CategorySerializer, ProductByCategorySerializer,
                          ReciptSerializer)
from main.models import (Stock, Product, Category, CheckIn, CheckOut, Shift,
                         Recipt)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView
from django.contrib.auth.models import User
from rest_framework.authentication import (TokenAuthentication,
                                           SessionAuthentication)
from datetime import datetime
from django.utils.timezone import get_current_timezone


class loadProductsAPIView(APIView):
    # permission_classes = [IsAdminUser]
    def get(self, request, *args, **kwargs):
        key = self.kwargs['key'].lower()

        # Sanity Check
        try:
            productObj = Product.objects.filter(name__icontains=key)[:10]
        except Product.DoesNotExist:
            return Response({'Error': _('Product does not exist')}, status=404)

        jResponse = []
        for product in productObj:
            jResponse.append({'id': product.pk, 'name': product.name})

        return Response(jResponse)


class searchProduct(APIView):
    # permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        key = request.data.get('key')
        category = request.data.get('category')
        category_obj = Category.objects.get(pk=int(category))

        # Sanity Check
        try:
            productObj = Product.objects.filter(name__icontains=key,
                                                category=category_obj)[:10]
        except Product.DoesNotExist:
            return Response({'Error': _('Product does not exist')}, status=404)

        jResponse = []
        for product in productObj:
            jResponse.append({'id': product.pk, 'name': product.name})

        return Response(jResponse)


class StockFromProductViewSet(ModelViewSet):
    """
    Stocks API
    """
    permission_classes = [
        IsAdminUser,
    ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    serializer_class = StockSerializer
    lookup_field = 'product'
    queryset = Stock.objects.all()


class StockViewSet(ModelViewSet):
    """
    Stocks API
    """
    permission_classes = [
        IsAdminUser,
    ]
    serializer_class = StockSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Stock.objects.all()


class ProductViewSet(ModelViewSet):
    """
    Products API
    """
    permission_classes = [
        IsAdminUser,
    ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class UserDetailsAPIView(RetrieveAPIView):
    model = User
    serializer_class = UserDetailSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_object(self):
        return self.request.user


class CheckInViewSet(mixins.CreateModelMixin, GenericViewSet):
    model = CheckIn
    serializer_class = CheckInSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        return CheckIn.objects.filter(user=self.request.user)


class CheckOutViewSet(mixins.CreateModelMixin, GenericViewSet):
    model = CheckOut
    serializer_class = CheckOutSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        return CheckIn.objects.filter(user=self.request.user)


class ShiftViewSet(mixins.ListModelMixin, GenericViewSet):
    model = Shift
    serializer_class = ShiftSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_queryset(self):
        return Shift.objects.filter(user=self.request.user,
                                    date=datetime.now(tz=get_current_timezone()))


class CategoryViewSet(mixins.ListModelMixin, GenericViewSet):
    model = Category
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    permission_classes = [
        IsAdminUser,
    ]

    def get_queryset(self):
        return Category.objects.all()


class ProductByCategoryAPIView(ListAPIView):
    serializer_class = ProductByCategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    lookup_field = 'category'

    permission_classes = [
        IsAdminUser,
    ]

    def get_queryset(self):
        try:
            category_obj = Category.objects.get(pk=self.kwargs['category'])
        except:
            category_obj = None
        finally:
            return Product.objects.filter(category=category_obj)


class ReciptViewSet(ModelViewSet):
    """
    Recipt API
    """
    permission_classes = [
        IsAdminUser,
    ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    serializer_class = ReciptSerializer
    queryset = Recipt.objects.all()
