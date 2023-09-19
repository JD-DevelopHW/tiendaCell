from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Supplier, Inventory
from .forms import CategoryForms, SupplierForm , InventoryForm

# Create your views here.

def listCategorys(request):

        categorys = Category.objects.filter(status=True)

        return render(request,'category.html', {
            'form': CategoryForms,
            'categorys': categorys
        })

    
def createCategory(request):
    
    try:
            form = CategoryForms(request.POST)
            form.save()
            return redirect('listCategorys')
    
    except ValueError:
         
        categorys = Category.objects.filter(status=True)

        return render(request,'category.html', {
            'form': CategoryForms,
            'categorys': categorys,
            'error': 'Por favor ingresar datos validos!'
        })
    
def editCategory(request, categoryId):
     
    if request.method == 'GET':
        
        findCategory = get_object_or_404(Category, pk=categoryId)
        form = CategoryForms(instance=findCategory)
        
        return render(request, 'categoryEdit.html', {
            'form': form,
            'category': findCategory
        })

    else:
        try:
            category = get_object_or_404(Category, pk=categoryId)
            form = CategoryForms(request.POST, instance=category)
            form.save()
            return redirect('listCategorys')
        except ValueError:
            return  render(request, 'categoryEditTemporal.html', {
            'form': form,
            'error': 'error actualizando categoria'
        })

def categoryRemove(request, categoryId):
    
    category = get_object_or_404(Category, pk=categoryId)
    
    if request.method == 'POST':
        category.status = False
        category.save()
        

    return redirect('listCategorys')

#<-------------------------------------Supplier----------------------------------->
def listSuppliers(request):

        suppliers = Supplier.objects.filter(status=True)

        return render(request,'supplier/suppliers.html', {
            'form': SupplierForm,
            'suppliers': suppliers
        })

def createSupplier(request):
    
    try:
        form = SupplierForm(request.POST)
        form.save()
        return redirect('listSuppliers')
    
    except ValueError:
         
        suppliers = Supplier.objects.filter(status=True)

        return render(request,'supplier/suppliers.html', {
            'form': SupplierForm,
            'suppliers': suppliers
        })
    
def supplierRemove(request, supplierId):
    
    supplier = get_object_or_404(Supplier, pk=supplierId)
    
    if request.method == 'POST':
            supplier.status = False
            supplier.save()
        

    return redirect('listSuppliers')



def editSupplier(request, supplierId):
     
    isupplier = get_object_or_404(Supplier, pk=supplierId)

    if request.method == 'GET':
        form = SupplierForm(instance=isupplier)
        return render(request, 'supplier/supplierEdit.html', {
            'form': form,
            'supplierId': isupplier.id
        })

    elif request.method == 'POST':
        form = SupplierForm(request.POST, instance=isupplier)
        
        if form.is_valid():
            form.save()
            return redirect('listSuppliers') 
        else:
            return render(request, 'supplier/supplierEdit.html', {
                'form': form,
                'supplier': isupplier
            })
        
#<-------------------------Invetory---------------------->


def inventario(request):

    iInventory = Inventory.objects.all()

    return render(request, 'inventario.html', {
         'form': InventoryForm,
         'inventories': iInventory
    })




def createInventory(request):
    
    try:
            form = InventoryForm(request.POST)
            form.save()
            return redirect('home')
    
    except ValueError:
         
        # categorys = Category.objects.filter(status=True)

        # return render(request,'category.html', {
        #     'form': CategoryForms,
        #     'categorys': categorys,
        #     'error': 'Por favor ingresar datos validos!'
        # })
        return redirect('home')
    

def editInventory(request, inventoryId):
     
    iInventory = get_object_or_404(Inventory, pk=inventoryId)

    if request.method == 'GET':
        form = InventoryForm(instance=iInventory)
        categoryName = iInventory.category.name
        supplierName = iInventory.supplier.name
        return render(request, 'inventoryEdit.html', {
            'form': form,
            'inventory': iInventory,
            'categoryName': categoryName,
            'supplierName': supplierName
        })

    elif request.method == 'POST':

        form = InventoryForm(request.POST, instance=iInventory)
        
        if form.is_valid():
            form.save()
            return redirect('home') 
        
        else:
            
            iInventory = Inventory.objects.all()

            return render(request, 'inventario.html', {
                'form': InventoryForm,
                'inventories': iInventory,
                'error': 'No se guardo'
            })

         
