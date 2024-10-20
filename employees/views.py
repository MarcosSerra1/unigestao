from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db import transaction
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from employees.forms import EmployeeModelForm, AddressModelForm, ContactInfoModelForm, FormOfPaymentModelForm, OfficeModelForm
from employees.models import Employee, ContactInfo, Address, FormOfPayment, EmployeeInventory, Office


class CreateOfficeView(CreateView):
    model = Office
    form_class = OfficeModelForm
    template_name = 'register_employee.html'  # Ou o nome do seu template que você está usando
    success_url = reverse_lazy('register_employee')  # Redireciona para a página de registro de funcionário após sucesso

    def form_valid(self, form):
        messages.success(self.request, 'Nova profissão criada com sucesso.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar a profissão.')
        return super().form_invalid(form)


@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(View):
    template_name = 'employees/home.html'

    def get(self, request):
        employee_inventory = EmployeeInventory.objects.first()
        if not employee_inventory:
            employee_inventory = EmployeeInventory(employee_count=0)
            employee_inventory.save()

        return render(
            request=request,
            template_name=self.template_name,
            context={
                'url': 'home',
                'employee_inventory': employee_inventory,
            }
        )


@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateEmployeeView(View):
    template_name = 'employees/register_employee.html'
    
    def get(self, request):
        person_form = EmployeeModelForm()
        contact_info_form = ContactInfoModelForm()
        address_form = AddressModelForm()
        form_of_payment_form = FormOfPaymentModelForm()

        return render(
            request=request,
            template_name=self.template_name, 
            context={
                'person_form': person_form,
                'contact_info_form': contact_info_form,
                'address_form': address_form,
                'form_of_payment_form': form_of_payment_form
            }
        )

    def post(self, request):
        person_form = EmployeeModelForm(request.POST)
        contact_info_form = ContactInfoModelForm(request.POST)
        address_form = AddressModelForm(request.POST)
        form_of_payment_form = FormOfPaymentModelForm(request.POST)

        if (person_form.is_valid() and contact_info_form.is_valid() and
            address_form.is_valid() and form_of_payment_form.is_valid()):
            with transaction.atomic():
                person = person_form.save()
                contact_info = contact_info_form.save(commit=False)
                contact_info.employee = person
                contact_info.save()
                
                address = address_form.save(commit=False)
                address.employee = person
                address.save()
                
                form_of_payment = form_of_payment_form.save(commit=False)
                form_of_payment.employee = person
                form_of_payment.save()

            messages.success(request, 'Funcionário cadastrado com sucesso.')   
            return redirect('/employee/') # Redirecione para uma página de sucesso

        return render(request, self.template_name, {
            'person_form': person_form,
            'contact_info_form': contact_info_form,
            'address_form': address_form,
            'form_of_payment_form': form_of_payment_form
        })


@method_decorator(login_required(login_url='login'), name='dispatch')
class EmployeesListView(ListView):
    model = Employee
    template_name = 'employees/list_persons.html'
    context_object_name = 'active_persons'  # Renomeie para active_persons

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            return Employee.objects.filter(name__icontains=search, status__status='Ativo').order_by('name')  # Filtra por ativos
        return Employee.objects.filter(status__status='Ativo').order_by('name')  # Apenas ativos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona a lista de funcionários inativos ao contexto
        context['inactive_persons'] = Employee.objects.filter(status__status='Inativo')  # Filtra por inativos
        return context



@method_decorator(login_required(login_url='login'), name='dispatch')
class EmployeesDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona o contato do funcionário ao contexto
        context['contact_info'] = ContactInfo.objects.get(employee=self.object)
        # Adiciona o endereço do funcionário ao contexto
        context['address'] = Address.objects.get(employee=self.object)
        # Adiciona a forma de pagamento do funcionário ao contexto
        context['form_of_payment'] = FormOfPayment.objects.get(employee=self.object)
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateEmployeeView(UpdateView):
    template_name = 'employees/update_employee.html'
    model = Employee
    form_class = EmployeeModelForm

    def get_success_url(self):
        messages.success(self.request, 'Funcionário Atualizado com Sucesso!')
        return reverse_lazy(
            'employee_details',
            kwargs={'pk': self.object.pk}
        )


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateContactView(UpdateView):
    template_name = 'employees/update_contact.html'
    model = ContactInfo
    form_class = ContactInfoModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona o funcionário ao contexto
        context['employee'] = self.object.employee
        return context
    
    def get_success_url(self):
        messages.success(self.request, 'Contato do Funcionário Atualizado com Sucesso!')
        return reverse_lazy(
            'employee_details',
            kwargs={'pk': self.object.employee.pk}
        )


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateAddressView(UpdateView):
    template_name = 'employees/update_address.html'
    model = Address
    form_class = AddressModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona o funcionário ao contexto
        context['employee'] = self.object.employee
        return context
    
    def get_success_url(self):
        messages.success(self.request, 'Endereço do Funcionário Atualizado com Sucesso!')
        return reverse_lazy(
            'employee_details',
            kwargs={'pk': self.object.employee.pk}
        )


@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateFormOfPayView(UpdateView):
    template_name = 'employees/update_form_of_payment.html'
    model = FormOfPayment
    form_class = FormOfPaymentModelForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona o funcionário ao contexto
        context['employee'] = self.object.employee
        return context

    def get_success_url(self):
        messages.success(self.request, 'Pix do Funcionário Atualizado com Sucesso!')
        return reverse_lazy(
            'employee_details',
            kwargs={'pk': self.object.employee.pk}
        )


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteEmployeeView(View):
    template_name = 'employees/delete_employee.html'

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, self.template_name, {'object': employee})
    
    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        messages.success(request, 'Funcionario Deletado com Sucesso!')
        return redirect('/employee/')
    

            
