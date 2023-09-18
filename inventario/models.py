from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150, null=True)
    cell_phone = models.IntegerField(null=False)
    status = models.BooleanField(default=True)

class Inventory(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30, null=True)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

