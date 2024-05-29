from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from employees.forms import PersonModelForm, AddressModelForm, ContactInfoModelForm, FormOfPaymentModelForm
from employees.models import Person
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class HomeView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='employees/home.html'
        )


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
                
            return redirect(reverse_lazy('/employee/'))  # Redirecione para uma página de sucesso

        return render(request, self.template_name, {
            'person_form': person_form,
            'contact_info_form': contact_info_form,
            'address_form': address_form,
            'form_of_payment_form': form_of_payment_form
        })
