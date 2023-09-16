from django.urls import path
from .views import listCategorys, createCategory,editCategory,inventario, categoryRemove


urlpatterns = [
    path('', inventario, name='home'),
    path('categorys/', listCategorys, name='listCategorys'),
    path('categorys/create/', createCategory, name='categorys_create'),
    path('categorys/edit/<int:categoryId>/', editCategory, name='category_edit'),
    path('categorys/remove/<int:categoryId>', categoryRemove, name='category_remove'),
]
