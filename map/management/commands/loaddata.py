from django.core.management.base import BaseCommand
from map.models import GroceryStoreAddresses, FarmersMarketAddresses
import csv
import traceback

class Command(BaseCommand):
    model = GroceryStoreAddresses
    model = FarmersMarketAddresses
    fields = ['address']
    fields = ['farmer_address']
    template_name = 'map.html'
    success_url = '/'

    def handle(self, *args, **kwargs):
        if not FarmersMarketAddresses.objects.exists():
            try:
                with open('./map/data/farmer_market.csv', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        FarmersMarketAddresses.objects.create(farmer_address=row['Street Address'])
            except Exception:
                traceback.print_exc()
        if not GroceryStoreAddresses.objects.exists():
            try:
                with open('./map/data/grocery_stores.csv', newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['Latitude'] != '' and row['Longitude'] != '':
                            GroceryStoreAddresses.objects.create(lat = row['Latitude'], long = row['Longitude'])
            except Exception:
                traceback.print_exc()
