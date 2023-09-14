from django.urls import path
from .views import listCategorys, createCategory,inventario

app_name = 'inventario'

urlpatterns = [
    path('', inventario),
    path('categorys/', listCategorys, name='categorys'),
    path('categorys/create/', createCategory, name='categorys_create'),
]
