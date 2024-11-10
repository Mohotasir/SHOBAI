from django.contrib import admin
from .models import User, MerchantApplication, Address, Zone, Area


# Register User model
admin.site.register(User)

# Register Merchant Application model
admin.site.register(MerchantApplication)

# Register Address model
admin.site.register(Zone)
admin.site.register(Area)
admin.site.register(Address)
