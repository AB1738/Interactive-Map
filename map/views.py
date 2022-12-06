from django.shortcuts import render  # noqa: F401
from django.views.generic import TemplateView, CreateView
from .models import GroceryStoreAddresses, FarmersMarketAddresses, FireHouseAddresses,SuperCenterAddresses


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutMeView(TemplateView):
    template_name = "aboutme.html"


class MapView(CreateView):
    model = GroceryStoreAddresses
    model = FarmersMarketAddresses
    model = FireHouseAddresses
    model = SuperCenterAddresses
    fields = ['address']
    fields = ['farmer_address']
    fields = ['fire_address']
    fields = ['supercenter_address']
    template_name = 'map.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            "access_token"] = 'pk.eyJ1IjoiaGFtc2llIiwiYSI6ImNsODN4aWdmcjBhNHEzcGw4ZXYxMHcxaXkifQ.67o9saEURWg3rF02gZxGKg'
        context['addresses'] = GroceryStoreAddresses.objects.all()
        context['farmer_addresses'] = FarmersMarketAddresses.objects.all()
        context['fire_addresses'] = FireHouseAddresses.objects.all()
        context['supercenter_addresses'] = SuperCenterAddresses.objects.all()
        return context
