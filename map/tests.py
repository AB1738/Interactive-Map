from django.test import TestCase
from map.models import GroceryStoreAddresses, FarmersMarketAddresses
import math
import geocoder


# Create your tests here.

class FarmerMarketAddressProcessingTestCase(TestCase):
    def setup(self):
        self.access_token = 'pk.eyJ1IjoiaGFtc2llIiwiYSI6ImNsODN4aWdmcjBhNHEzcGw4ZXYxMHcxaXkifQ.67o9saEURWg3rF02gZxGKg'
        self.address_model = FarmersMarketAddresses(farmer_address="535 MARCY AVE")

    def test_address_processing(self):
        g = geocoder.mapbox(self.address_model.farmer_address, key=self.access_token)
        latlong = g.latlng
        self.assertEqual(math.trunc(latlong[0]), 40)
        self.assertEqual(math.trunc(latlong[1]), -73)


class GroceryStoreTestCase(TestCase):
    def setup(self):
        GroceryStoreAddresses.objects.create(lat="40", long="-73")

    def test_grocery_store_saved(self):
        grocery_store = GroceryStoreAddresses.objects.get(lat__exact="40")
        self.assertEqual(grocery_store.long, -73.0)
