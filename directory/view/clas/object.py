from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from directory.forms import Object_ModelForm
from directory.models import Object


class ListObject(ListView):
    model = Object
    template_name = 'directory/object/list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Object.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Object.objects.all(), key=lambda x: x.name, reverse=True)
        return Object.objects.all()


    def get_context_data(self, **kwargs):
        context = super(ListObject, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        
        if search is not None:
            object_filter = Object.objects.filter(name__icontains=search)
            context['object_filter'] = object_filter
        return context


class DetailObject(DetailView):
    model = Object
    template_name = 'directory/object/detail.html'
    context_object_name = 'objects'


class CreateObject(CreateView):
    model = Object
    # fields = ('name', )
    template_name = 'directory/object/create_update.html'
    success_url = reverse_lazy('sensor')
    form_class = Object_ModelForm




class UpdateObject(UpdateView):
    model = Object
    template_name = 'directory/object/create_update.html'
    success_url = reverse_lazy('object')
    context_object_name = 'objects'
    form_class = Object_ModelForm


class DeleteObject(DeleteView):
    model = Object
    success_url = reverse_lazy('object')
    context_object_name = 'objects'
    template_name = 'directory/object/delete.html'
