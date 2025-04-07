from django.db import models

# Create your models here.


class Menuitem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics')