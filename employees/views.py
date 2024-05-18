from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from employees.forms import PersonModelForm, AddressModelForm, ContactInfoModelForm, FormOfPaymentModelForm
from employees.models import Person


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


class EmployeeCreateView(CreateView):
    model = Person
    form_class = PersonModelForm
    template_name = 'employees/register_person.html'
    success_url = '/register/address/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_person_form'] = context['form']
        return context


class AddressCreateView(CreateView):
    model = Person
    form_class = AddressModelForm
    template_name = 'employees/register_address.html'
    success_url = '/register/contact/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_address_form'] = context['form']
        return context


class ContactCreateView(CreateView):
    model = Person
    form_class = ContactInfoModelForm
    template_name = 'employees/register_contact.html'
    success_url = '/register/form_of_pay/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_contact_form'] = context['form']
        return context


class PayCreateView(CreateView):
    model = Person
    form_class = FormOfPaymentModelForm
    template_name = 'employees/register_form_payment.html'
    success_url = '/employee/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_formofpay_form'] = context['form']
        return context
