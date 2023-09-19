from django.forms import ModelForm, ModelChoiceField
from .models import Category, Supplier, Inventory


class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','address','cell_phone']


class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name','code','amount','price','category','supplier']
    
    category = ModelChoiceField(queryset=Category.objects.filter(status=True))
    
    supplier = ModelChoiceField(queryset=Supplier.objects.filter(status=True))
        


