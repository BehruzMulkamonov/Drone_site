from django.shortcuts import render, redirect
from spravchnik.forms import RegionModelForm
from spravchnik.models import Region


def index(request):
    search = request.GET.get('search')

    if search is not None:
        region_filter = Region.filter(name__startwith=search)
        return render(request, 
                      'spravchnik/region/list.html',
                       {'region_filter': region_filter} )
    else:
        regions = Region.objects.all()
        return render(request, 'spravchnik/region/list.html', {"regions": regions})

def delet_region(request, pk):
    region = Region.objects.get(pk=pk)
    region.delete
    return redirect('index')

def create_region(request):
    if request.method == 'POST':
        form = RegionModelForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = RegionModelForm()
        return render(request, 'spravchnik/region/create_update.html', {"form": form})
    

def update_brand(request, pk):
    region = Region.objects.get(pk=pk)
    if request.method == "POST":
        form = RegionModelForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegionModelForm(instance=region)
        return render(request, 'spravchnik/region/update_brand.html', {"form": form, "region": region})
