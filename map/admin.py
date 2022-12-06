from django.contrib import admin 
from .models import GroceryStoreAddresses, FarmersMarketAddresses, FireHouseAddresses, Super_CenterAddresses

admin.site.register(GroceryStoreAddresses)
admin.site.register(FarmersMarketAddresses)
admin.site.register(Super_CenterAddresses)
admin.site.register(FireHouseAddresses)
