from django.test import TestCase 
from map.models import GroceryStoreAddresses
import math
import geocoder
# Create your tests here.

class GroceryStoreAddressProcessingTestCase(TestCase):
    def test_address_processing(self):
        access_token='pk.eyJ1IjoiaGFtc2llIiwiYSI6ImNsODN4aWdmcjBhNHEzcGw4ZXYxMHcxaXkifQ.67o9saEURWg3rF02gZxGKg'
        testModle = GroceryStoreAddresses(address="115 E 68th St, New York, NY 10065")
        g=geocoder.mapbox(testModle.address,key=access_token)
        latlong = g.latlng
        print(math.trunc(latlong[0]))
        print(math.trunc(latlong[1]))
        return(math.trunc(latlong[0])==40 and math.trunc(latlong[1])==-73)
