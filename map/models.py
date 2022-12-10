from django.db import models 
import geocoder


access_token='pk.eyJ1IjoiYXJpZWxiMSIsImEiOiJjbGIxbnFyNW4wNXVjM3dueW5lbGVoeDRnIn0.8_79cvoMd9lBAUQKUe27tA'
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

class SuperMarketAddresses(models.Model):
    supermarket_address = models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

class SupercenterAddresses(models.Model):
    supercenter_address = models.TextField()
    lat=models.FloatField(blank=True,null=True)
    long=models.FloatField(blank=True,null=True)

