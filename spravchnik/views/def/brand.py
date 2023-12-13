from django.shortcuts import render, redirect
from spravchnik.forms import BrandModelForm, CategoryModelForm
from spravchnik.models import Brand, Category


def index(request):
    search = request.GET.get('search')

    if search is not None:
        brand_filter = Brand.filter(name__startwith=search)
        return render(request, 
                      'spravchnik/brand/list.html',
                       {'branmd_filter': brand_filter} )
    else:
        brands = Brand.objects.all()
        return render(request, 'spravchnik/brand/list.html', {"brands": brands})

def delet_brand(request, pk):
    brand = Brand.objects.get(pk=pk)
    brand.delete
    return redirect('index')

def create_brand(request):
    if request.method == 'POST':
        form = BrandModelForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = BrandModelForm()
        return render(request, 'spravchnik/brand/create_update.html', {"form": form})
    
# instance - o'rniga qo'yish degani
def update_brand(request, pk):
    brand = Brand.objects.get(pk=pk)
    if request.method == "POST":
        form = BrandModelForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BrandModelForm(instance=brand)
        return render(request, 'spravchnik/brand/update_brand.html', {"form": form, "brand": brand})
