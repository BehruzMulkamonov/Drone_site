from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import SensortypeModelForm
from spravchnik.models import Sensortype


class ListType(ListView):
    model = Sensortype
    template_name = 'spravchnik/sensortype/list.html'
    context_object_name = 'sensortype'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Sensortype.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Sensortype.objects.all(), key=lambda x: x.name, reverse=True)
        return Sensortype.objects.all()


    def get_context_data(self, **kwargs):
        context = super(ListType, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            sensortype_filter = Sensortype.objects.filter(name__startswith=search)
            context['sensortype_filter'] = sensortype_filter

        return context


class DetailType(DetailView):
    model = Sensortype
    template_name = 'spravchnik/sensortype/detail.html'
    context_object_name = 'sensortype'


class CreateType(CreateView):
    model = Sensortype
    # fields = ('name', )
    template_name = 'spravchnik/sensortype/create_update.html'
    success_url = reverse_lazy('sensortype')
    form_class = SensortypeModelForm

    # def get(self, request, *args, **kwargs):
    #     # form = BrandModelForm(request.GET)
    #     # print(form)
    #     return super().get(request, *args, **kwargs)


class UpdateType(UpdateView):
    model = Sensortype
    # fields = ('name', )
    template_name = 'spravchnik/sensortype/create_update.html'
    success_url = reverse_lazy('sensortype')
    context_object_name = 'sensortype'
    form_class = SensortypeModelForm


class DeleteType(DeleteView):
    model = Sensortype
    success_url = reverse_lazy('sensortype')
    context_object_name = 'sensortype'
    template_name = 'spravchnik/sensortype/delete.html'
