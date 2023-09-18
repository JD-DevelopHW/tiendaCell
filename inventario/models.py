from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    # def clean_name(self):
    #     name = self.name

        # if len(name) < 5:
        #     raise ValidationError("El nombre debe tener al menos 5 caracteres.")

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

