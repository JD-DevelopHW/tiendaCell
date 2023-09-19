from django.urls import path
from .views import listCategorys, createCategory,editCategory,inventario, categoryRemove, listSuppliers, createSupplier, supplierRemove, editSupplier, createInventory, editInventory



urlpatterns = [
    path('', inventario, name='home'),
    path('categorys/', listCategorys, name='listCategorys'),
    path('categorys/create/', createCategory, name='categorys_create'),
    path('categorys/edit/<int:categoryId>/', editCategory, name='category_edit'),
    path('categorys/remove/<int:categoryId>', categoryRemove, name='category_remove'),
    path('supplier/', listSuppliers, name='listSuppliers'),
    path('supplier/create/', createSupplier, name='createSuppliers'),
    path('supplier/edit/<int:supplierId>/', editSupplier, name='supplier_edit'), 
    path('supplier/remove/<int:supplierId>', supplierRemove, name='supplier_remove'),
    path('Inventory/create/', createInventory, name='createInventory'),
    path('Inventory/edit/<int:inventoryId>/', editInventory, name='inventory_edit'),
]
