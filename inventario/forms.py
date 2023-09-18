from django.forms import ModelForm
from .models import Category, Supplier


class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','address','cell_phone']
        


