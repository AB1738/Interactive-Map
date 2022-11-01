from django.test import TestCase 
from map.models import GroceryStoreAddresses, FarmersMarketAddresses
import math
import geocoder
# Create your tests here.

class FarmerMarketAddressProcessingTestCase(TestCase):
    def test_address_processing(self):
        access_token='pk.eyJ1IjoiaGFtc2llIiwiYSI6ImNsODN4aWdmcjBhNHEzcGw4ZXYxMHcxaXkifQ.67o9saEURWg3rF02gZxGKg'
        testModel = FarmersMarketAddresses(farmer_address="535 MARCY AVE")
        g=geocoder.mapbox(testModel.farmer_address,key=access_token)
        latlong = g.latlng
        print(math.trunc(latlong[0]))
        print(math.trunc(latlong[1]))
        self.assertEqual(math.trunc(latlong[0]),40)
        self.assertEqual(math.trunc(latlong[1]), -73)


