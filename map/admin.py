from django.contrib import admin 
from .models import GroceryStoreAddresses, FarmersMarketAddresses, FireHouseAddresses, SuperCenterAddresses

admin.site.register(GroceryStoreAddresses)
admin.site.register(FarmersMarketAddresses)
admin.site.register(FireHouseAddresses)
admin.site.register(SuperCenterAddresses)