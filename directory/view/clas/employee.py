from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, CreateView, UpdateView, DetailView

from directory.forms import Emp_ModelForm
from directory.models import Employee


class ListEmp(ListView):
    model = Employee
    template_name = 'directory/employee/list.html'
    context_object_name = 'employee'

    def get_queryset(self):
        order = self.request.GET.get('order')
        if order is not None:
            if order == 'asc':
                return sorted(Employee.objects.all(), key=lambda x: x.name)
            else:
                return sorted(Employee.objects.all(), key=lambda x: x.name, reverse=True)
        return Employee.objects.all()


    def get_context_data(self, **kwargs):
        context = super(ListEmp, self).get_context_data(**kwargs)
        search = self.request.GET.get('search')
        
        if search is not None:
            employee_filter = Employee.objects.filter(first_name__icontains=search)
            context['employee_filter'] = employee_filter
        return context


class DetailEmp(DetailView):
    model = Employee
    template_name = 'directory/employee/detail.html'
    context_object_name = 'employee'


class CreateEmp(CreateView):
    model = Employee
    # fields = ('name', )
    template_name = 'directory/employee/create_update.html'
    success_url = reverse_lazy('employee')
    form_class = Emp_ModelForm

    def get(self, request, *args, **kwargs):
        # form = BrandModelForm(request.GET)
        # print(form)
        return super().get(request, *args, **kwargs)


class UpdateEmp(UpdateView):
    model = Employee
    # fields = ('name', )
    template_name = 'directory/employee/create_update.html'
    success_url = reverse_lazy('employee')
    context_object_name = 'employee'
    form_class = Emp_ModelForm


class DeleteEmp(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee')
    context_object_name = 'employee'
    template_name = 'directory/employee/delete.html'
