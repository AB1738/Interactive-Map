from django.shortcuts import render #noqa: F401
from django.views.generic import TemplateView, CreateView
from .models import GroceryStoreAddresses


class HomePageView(TemplateView):
    template_name = "home.html"


class MapView(CreateView):
    model=GroceryStoreAddresses
    fields=['address']
    template_name='map.html'
    success_url='/'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["access_token"]= 'pk.eyJ1IjoiaGFtc2llIiwiYSI6ImNsODN4aWdmcjBhNHEzcGw4ZXYxMHcxaXkifQ.67o9saEURWg3rF02gZxGKg'
        context['addresses']=GroceryStoreAddresses.objects.all()
        return context

