from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

class Inventory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

