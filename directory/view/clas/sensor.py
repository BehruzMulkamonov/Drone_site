from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from directory.forms import Sensor_ModelForm
from directory.models import Sensor


class ListSensor(ListView):
    model = Sensor
    template_name = 'directory/sensor/list.html'
    context_object_name = 'sensors'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Sensor.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Sensor.objects.all(), key=lambda x: x.name, reverse=True)
        return Sensor.objects.all()


    def get_context_data(self, **kwargs):
        context = super(ListSensor, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        
        if search is not None:
            sensors_filter = Sensor.objects.filter(name__icontains=search)
            context['sensors_filter'] = sensors_filter
        return context


class DetailSensor(DetailView):
    model = Sensor
    template_name = 'directory/sensor/detail.html'
    context_object_name = 'sensor'


class CreateSensor(CreateView):
    model = Sensor
    # fields = ('name', )
    template_name = 'directory/sensor/create_update.html'
    success_url = reverse_lazy('sensor')
    form_class = Sensor_ModelForm

    def get(self, request, *args, **kwargs):
        # form = BrandModelForm(request.GET)
        # print(form)
        return super().get(request, *args, **kwargs)


class UpdateSensor(UpdateView):
    model = Sensor
    # fields = ('name', )
    template_name = 'directory/sensor/create_update.html'
    success_url = reverse_lazy('sensor')
    context_object_name = 'sensor'
    form_class = Sensor_ModelForm


class DeleteSensor(DeleteView):
    model = Sensor
    success_url = reverse_lazy('sensor')
    context_object_name = 'sensor'
    template_name = 'directory/sensor/delete.html'
