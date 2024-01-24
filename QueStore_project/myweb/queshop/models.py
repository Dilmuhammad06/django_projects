from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30),
    old_price = models.CharField(max_length=30),
    new_price = models.CharField(max_length=30)