from django.core.management.base import BaseCommand
from map.models import GroceryStoreAddresses, FarmersMarketAddresses, FireHouseAddresses
from enum import Enum
import csv
import traceback


class ModelType(Enum):
    FarmerMarket = 1
    GroceryStore = 2
    Firehouses = 3


class Command(BaseCommand):
    model = GroceryStoreAddresses
    model = FarmersMarketAddresses
    fields = ['address']
    fields = ['farmer_address']
    template_name = 'map.html'
    success_url = '/'

    def __process_csv(self, **kwargs):
        try:
            with open(kwargs['Path'], newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    match kwargs['ObjectType']:
                        case ModelType.FarmerMarket:
                            FarmersMarketAddresses.objects.create(farmer_address=row['Street Address'])
                        case ModelType.GroceryStore:
                            if row['Latitude'] != '' and row['Longitude'] != '':
                                GroceryStoreAddresses.objects.create(lat=row['Latitude'], long=row['Longitude'])
                        case ModelType.Firehouses:
                            if row['Latitude'] != '' and row['Longitude'] != '':
                                FireHouseAddresses.objects.create(lat=row['Latitude'], long=row['Longitude'])
                        case _:
                            return
        except Exception:
            traceback.print_exc()

    def handle(self, *args, **kwargs):
        DATA_ROOT = './map/data/'
        FARMER_MARKET_PATH = DATA_ROOT + 'farmer_market.csv'
        GROCERY_STORE_PATH = DATA_ROOT + 'grocery_stores.csv'
        FIREHOUSE_PATH = DATA_ROOT + 'firehouses.csv'
        if not FarmersMarketAddresses.objects.exists():
            self.__process_csv(ObjectType=ModelType.FarmerMarket, Path=FARMER_MARKET_PATH)
        if not GroceryStoreAddresses.objects.exists():
            self.__process_csv(ObjectType=ModelType.GroceryStore, Path=GROCERY_STORE_PATH)
        if not FireHouseAddresses.objects.exists():
            self.__process_csv(ObjectType=ModelType.Firehouses, Path=FIREHOUSE_PATH)
