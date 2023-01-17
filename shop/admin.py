from django.contrib import admin

from shop.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_image', 'product_price', 'product_collection']

admin.site.register(Product, ProductAdmin)