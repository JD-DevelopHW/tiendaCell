from django.forms import ModelForm, ValidationError
from .models import Category, Supplier


class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 5:
    #         raise ValidationError("El nombre debe tener al menos 5 caracteres.")
    #     return name

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','address','cell_phone']
        


