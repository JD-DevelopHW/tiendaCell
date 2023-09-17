from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForms

# Create your views here.

def inventario(request):

    return render(request, 'inventario.html')

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
         
        categorys = Category.objects.all()

        return render(request,'category.html', {
            'form': CategoryForms,
            'categorys': categorys,
            'error': 'Por favor ingresar datos validos!'
        })
    
def editCategory(request, categoryId):
     
    if request.method == 'GET':
        
        findCategory = get_object_or_404(Category, pk=categoryId)
        form = CategoryForms(instance=findCategory)
        
        
        return render(request, 'categoryEditTemporal.html', {
            'form': form,
            'category': findCategory
        })

    else:
        try:
            category = get_object_or_404(Category, pk=categoryId)
            form = CategoryForms(request.POST, instance=category)
            print(form)
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

         
