from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
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


def new_person_view(request):
    if request.method == 'POST':
        new_person_form = PersonModelForm(request.POST)
        if new_person_form.is_valid():
            new_person_form.save()
            return redirect('register_address')
    else:
        new_person_form = PersonModelForm()

    return render(
        request=request,
        template_name='employees/register_person.html',
        context={ 'new_person_form': new_person_form }
    )


def new_address_view(request):
    if request.method == 'POST':
        new_address_form = AddressModelForm(request.POST)
        if new_address_form.is_valid():
            new_address_form.save()
            return redirect('register_contact')
    else:
        new_address_form = AddressModelForm()
    return render(
        request=request,
        template_name='employees/register_address.html',
        context={ 'new_address_form': new_address_form}
    )


def new_contact_view(request):
    if request.method == 'POST':
        new_contact_form = ContactInfoModelForm(request.POST)
        if new_contact_form.is_valid():
            new_contact_form.save()
            return redirect('register_formofpayment')
    else:
        new_contact_form = ContactInfoModelForm()
    return render(
        request=request,
        template_name='employees/register_contact.html',
        context={ 'new_contact_form':new_contact_form }
    )


def new_formofpay_view(request):
    if request.method == 'POST':
        new_formofpay_form = FormOfPaymentModelForm(request.POST)
        if new_formofpay_form.is_valid():
            new_formofpay_form.save()
            return redirect('employee')
    else:
        new_formofpay_form = FormOfPaymentModelForm()
    return render(
        request=request,
        template_name='employees/register_form_payment.html',
        context={ 'new_formofpay_form':new_formofpay_form }
    )
