from django.contrib import admin
from .models import User, MerchantApplication


# Register User model
admin.site.register(User)

# Register Merchant Application model
admin.site.register(MerchantApplication)
