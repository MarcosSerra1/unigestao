from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db import transaction
from django.views.generic import ListView, DetailView, UpdateView
from employees.forms import PersonModelForm, AddressModelForm, ContactInfoModelForm, FormOfPaymentModelForm
from employees.models import Person, ContactInfo, Address, FormOfPayment

class HomeView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='employees/home.html'
        )


class CreateEmployeeView(View):
    template_name = 'employees/register_employee.html'
    
    def get(self, request):
        person_form = PersonModelForm()
        contact_info_form = ContactInfoModelForm()
        address_form = AddressModelForm()
        form_of_payment_form = FormOfPaymentModelForm()

        return render(request, self.template_name, {
            'person_form': person_form,
            'contact_info_form': contact_info_form,
            'address_form': address_form,
            'form_of_payment_form': form_of_payment_form
        })

    def post(self, request):
        person_form = PersonModelForm(request.POST)
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


class EmployeesListView(ListView):
    model = Person
    template_name = 'employees/list_persons.html'
    context_object_name = 'persons'

    def get_queryset(self):
        person = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
            person = Person.objects.filter(name__icontains=search)
        return person


class EmployeesDetailView(DetailView):
    model = Person
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


class UpdateEmployeeView(UpdateView):
    template_name = 'employees/update_employee.html'
    model = Person
    form_class = PersonModelForm

    def get_success_url(self):
        return reverse_lazy(
            'employee_details',
            kwargs={'pk': self.object.pk}
        )


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
        return reverse_lazy(
            'employee_details',
            kwargs={'pk': self.object.employee.pk}
        )


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
        return reverse_lazy(
            'employee_details',
            kwargs={'pk': self.object.employee.pk}
        )


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
        return reverse_lazy(
            'employee_details',
            kwargs={'pk': self.object.employee.pk}
        )


class DeleteEmployeeView(View):
    template_name = 'employees/delete_employee.html'

    def get(self, request, pk):
        employee = get_object_or_404(Person, pk=pk)
        return render(request, self.template_name, {'object': employee})
    
    def post(self, request, pk):
        employee = get_object_or_404(Person, pk=pk)
        employee.delete()
        messages.success(request, 'Funcionario Deletado com Sucesso!')
        return redirect('/employee/')
