# from django.utils.translation import gettext as _
from .permissions import IsAdminUser
# from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.viewsets import ModelViewSet
from .serializers import StockSerializer, ProductSerializer
from main.models import Stock, Product
from rest_framework.views import APIView
from rest_framework.response import Response


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
            jResponse.append({
                'id': product.pk,
                'name': product.name
            })

        return Response(jResponse)


class StockFromProductViewSet(ModelViewSet):
    """
    Stocks API
    """
    permission_classes = [IsAdminUser, ]
    serializer_class = StockSerializer
    lookup_field = 'product'
    queryset = Stock.objects.all()


class StockViewSet(ModelViewSet):
    """
    Stocks API
    """
    permission_classes = [IsAdminUser, ]
    serializer_class = StockSerializer
    queryset = Stock.objects.all()


class ProductViewSet(ModelViewSet):
    """
    Products API
    """
    permission_classes = [IsAdminUser, ]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
