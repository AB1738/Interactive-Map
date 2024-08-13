from django.shortcuts import render  # noqa: F401
from django.views.generic import TemplateView, CreateView
from .models import GroceryStoreAddresses, FarmersMarketAddresses, FireHouseAddresses, SupercenterAddresses, SuperMarketAddresses
import os
from dotenv import load_dotenv

class HomePageView(TemplateView):
    template_name = "home.html"


class AboutMeView(TemplateView):
    template_name = "aboutme.html"


class MapView(CreateView):
    model = GroceryStoreAddresses
    model = FarmersMarketAddresses
    model = FireHouseAddresses
    model = SupercenterAddresses
    model = SuperMarketAddresses
    fields = ['address']
    fields = ['farmer_address']
    fields = ['fire_address']
    fields = ['supercenter_address']
    fields = ['supermarket_address']
    template_name = 'map.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "access_token"] = os.getenv('MAPBOX_TOKEN')
        context['addresses'] = list(GroceryStoreAddresses.objects.values())
        context['farmer_addresses'] = list(FarmersMarketAddresses.objects.values())
        context['fire_addresses'] = list(FireHouseAddresses.objects.values())
        context['supercenter_addresses'] = list(SupercenterAddresses.objects.values())
        context['supermarket_addresses'] = list(SuperMarketAddresses.objects.values())
        return context
