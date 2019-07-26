from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=19, decimal_places=2)
    quantity = models.PositiveSmallIntegerField()
    manufacturer = models.ForeignKey(Manufacturer, 
                                     on_delete=models.CASCADE, 
                                     related_name="products")

    def __str__(self):
        return self.name