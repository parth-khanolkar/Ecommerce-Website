from django.contrib import admin

from cart.models import Cart, Cartitem, Shipping

# Register your models here.
admin.site.register(Cart)
admin.site.register(Cartitem)
admin.site.register(Shipping)