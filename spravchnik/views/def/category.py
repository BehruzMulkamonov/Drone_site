from django.shortcuts import render, redirect
from spravchnik.forms import BrandModelForm, CategoryModelForm
from spravchnik.models import Brand, Category


    

# Category

def index(request):
    search = request.GET.get('search')

    if search is not None:
        category_filter = Category.filter(name__startwith=search)
        return render(request, 
                      'spravchnik/list.html',
                       {'category_filter': category_filter} )
    else:
        categories = Category.objects.all()
        return render(request, 'spravchnik/list.html', {"categories": categories})

def delet_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete
    return redirect('index')

def create_category(request):
    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = CategoryModelForm()
        return render(request, 'spravchnik/create_update.html', {"form": form})
    

def update_brand(request, pk):
    brand = Category.objects.get(pk=pk)
    if request.method == "POST":
        form = CategoryModelForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryModelForm(instance=brand)
        return render(request, 'spravchnik/update_brand.html', {"form": form, "brand": brand})

