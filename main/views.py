# from django.shortcuts import render
from django.views.generic import (ListView, TemplateView)
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Stock, Category, Recipt
# from django.http import JsonResponse
# from django.http import HttpResponseRedirect
# import json


class StockListView(LoginRequiredMixin, ListView):
    "Main Home Page"
    model = Stock
    paginate_by = 20
    template_name = 'main/index.html'


class StockAddPage(LoginRequiredMixin, TemplateView):
    template_name = 'main/add_stock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class StockRemovePage(LoginRequiredMixin, TemplateView):
    template_name = 'main/remove_stock.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class ProductPage(LoginRequiredMixin, TemplateView):
    template_name = 'main/product.html'


class ReciptCreate(LoginRequiredMixin, CreateView):
    template_name = 'main/add_recipt.html'
    model = Recipt
    fields = '__all__'
    success_url = reverse_lazy('main:success-recipt')


class ReciptListView(LoginRequiredMixin, ListView):
    "Main Recipt Page"
    model = Recipt
    paginate_by = 20
    template_name = 'main/recipt_list.html'


class ReciptSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'main/success_recipt.html'
