from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Product(models.Model):
    COLLECTIONS = {
        ('LR', 'LivingRoom'),
        ('BR', 'BedRoom'),
        ('K', 'Kitchen'),
        ('NA', 'New-Arrivals')
    }

    product_image = models.ImageField(upload_to='images')
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=1000)
    product_price = models.IntegerField()
    product_collection = MultiSelectField(choices=COLLECTIONS)

    def __str__(self):
        return self.product_name