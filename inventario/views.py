from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForms

# Create your views here.

def inventario(request):

    return render(request, 'inventario.html')

def listCategorys(request):

        categorys = Category.objects.all()

        return render(request,'category.html', {
            'form': CategoryForms,
            'categorys': categorys
        })

    
def createCategory(request):
    form = CategoryForms(request.POST)
    form.save()

    return redirect('/categorys/')
