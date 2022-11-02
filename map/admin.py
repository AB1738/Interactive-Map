from django.contrib import admin 
from .models import GroceryStoreAddresses, FarmersMarketAddresses, FireHouseAddresses

admin.site.register(GroceryStoreAddresses)
admin.site.register(FarmersMarketAddresses)
admin.site.register(FireHouseAddresses)