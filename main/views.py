# from django.shortcuts import render
from django.views.generic import (ListView, TemplateView)
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse_lazy
from .models import Stock
# from django.http import JsonResponse
# from django.http import HttpResponseRedirect
# import json


class StockListView(ListView):
    "Main Home Page"
    model = Stock
    paginate_by = 20
    template_name = 'main/index.html'


class StockChangePage(TemplateView):
    template_name = 'main/stock_change.html'


class ProductPage(TemplateView):
    template_name = 'main/product.html'
