from django.shortcuts import render
from .models import Employee
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, Paginator


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'base/update.html'
    success_url = reverse_lazy('list')



class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    context_object_name = 'employee'
    success_url = reverse_lazy('list')
    template_name = 'base/delete.html'

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'base/detail.html'

class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('list')
    template_name = 'base/create.html'



class ClientLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')


class ClientRegister(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(ClientRegister, self).form_valid(form)


@login_required
def employees_list(request):
    employees = Employee.objects.all()
    valid_type = ''
    valid_cat = ''
    if request.method == 'POST':
        if request.POST.get('ID') != '':
            valid_cat = request.POST.get('ID')
            employees = employees.filter(pk=valid_cat)
            valid_type = 'ID'

        if request.POST.get('fullname') != '':
            valid_cat = request.POST.get('fullname')
            employees = employees.filter(full_name__icontains=valid_cat)
            valid_type = 'fullname'


        if request.POST.get('pos') != '':
            valid_cat = request.POST.get('pos')
            employees = employees.filter(position=valid_cat)
            valid_type = 'pos'


        if request.POST.get('zp') != '':
            valid_cat = request.POST.get('zp')
            employees = employees.filter(salary=valid_cat)
            valid_type = 'zp'


        if request.POST.get('employdate') != '':
            valid_cat = request.POST.get('employdate')
            employees = employees.filter(employment_date=valid_cat)
            valid_type = 'employdate'


        if request.POST.get('boss') != '':
            valid_cat = request.POST.get('boss')
            employees = Employee.objects.filter(boss=valid_cat)
            valid_type = 'boss'

        page_obj = employees
        return render(request, 'base/list.html', {'page_obj': page_obj})


    elif request.method == 'GET':
        order = request.GET.get('order')
        type_column = request.GET.get('cat')

        if order == 'desc':
            employees = employees.order_by(type_column).reverse()

        elif order == 'asc':
            employees = employees.order_by(type_column)


        paginator = Paginator(employees, 100)
        try:
            page_obj = paginator.page(request.GET.get('page'))
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)


        get_copy = request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()

        return render(request, 'base/list.html', {'page_obj': page_obj, 'data': employees, 'parameters': parameters})

