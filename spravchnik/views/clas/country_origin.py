from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from spravchnik.forms import Country_origin_ModelForm
from spravchnik.models import Country_origin


class ListOrigin(ListView):
    model = Country_origin
    template_name = 'spravchnik/origin/list.html'
    context_object_name = 'Country_origins'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Country_origin.objects.all(), key=lambda x: x.name)

            else:
                return sorted(Country_origin.objects.all(), key=lambda x: x.name, reverse=True)
        return Country_origin.objects.all()


    def get_context_data(self, **kwargs):
        context = super(ListOrigin, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')

        if search is not None:
            origin_filter = Country_origin.objects.filter(name__startswith=search)
            context['origin_filter'] = origin_filter

        return context


class DetailOrigin(DetailView):
    model = Country_origin
    template_name = 'spravchnik/origin/detail.html'
    context_object_name = 'Country_origin'


class CreateOrigin(CreateView):
    model = Country_origin
    # fields = ('name', )
    template_name = 'spravchnik/origin/create_update.html'
    success_url = reverse_lazy('origin')
    form_class = Country_origin_ModelForm

    def get(self, request, *args, **kwargs):
        # form = BrandModelForm(request.GET)
        # print(form)
        return super().get(request, *args, **kwargs)


class UpdateOrigin(UpdateView):
    model = Country_origin
    # fields = ('name', )
    template_name = 'spravchnik/origin/create_update.html'
    success_url = reverse_lazy('origin')
    context_object_name = 'Country_origin'
    form_class = Country_origin_ModelForm


class DeleteOrigin(DeleteView):
    model = Country_origin
    success_url = reverse_lazy('origin')
    context_object_name = 'Country_origin'
    template_name = 'spravchnik/origin/delete.html'
