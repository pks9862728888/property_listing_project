from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, related_name='realtors',
                                on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=7, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo4 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo5 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo6 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title