from django.forms import ModelForm
from .models import Category


class CategoryForms(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        


