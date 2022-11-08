from django.db import models 
import geocoder


access_token='pk.eyJ1IjoiaGFtc2llIiwiYSI6ImNsODN4aWdmcjBhNHEzcGw4ZXYxMHcxaXkifQ.67o9saEURWg3rF02gZxGKg'
class GroceryStoreAddresses(models.Model):
    address=models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

class FarmersMarketAddresses(models.Model):
    farmer_address=models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

    def save(self, *args, **kwargs):
        g=geocoder.mapbox(self.farmer_address,key=access_token)
        g=g.latlng
        self.lat=g[0]
        self.long=g[1]
        super(FarmersMarketAddresses,self).save(*args,**kwargs)

class FireHouseAddresses(models.Model):
    fire_address=models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

