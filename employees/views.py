from django.shortcuts import render, redirect
from employees.forms import PersonModelForm, AddressModelForm, ContactInfoModelForm, FormOfPaymentModelForm
from employees.models import Person

def home_view(request):
    return render(
        request=request,
        template_name='home.html'
    )


def list_persons_view(request):
    persons = Person.objects.all()
    return render(
        request=request,
        template_name='list_persons.html',
        context={ 'persons': persons })


def new_person_view(request):
    if request.method == 'POST':
        new_person_form = PersonModelForm(request.POST)
        if new_person_form.is_valid():
            new_person_form.save()
            return redirect('address/')
    else:
        new_person_form = PersonModelForm()

    return render(
        request=request,
        template_name='register_person.html',
        context={ 'new_person_form': new_person_form }
    )


def new_address_view(request):
    if request.method == 'POST':
        new_address_form = AddressModelForm(request.POST)
        if new_address_form.is_valid():
            new_address_form.save()
            return redirect('employee')
    else:
        new_address_form = AddressModelForm()
    return render(
        request=request,
        template_name='register_address.html',
        context={ 'new_address_form': new_address_form}
    )


def new_contact_view(request):
    if request.method == 'POST':
        new_contact_form = ContactInfoModelForm(request.POST)
        if new_contact_form.is_valid():
            new_contact_form.save()
            return('')  # colocar um redirect
    else:
        new_contact_form = ContactInfoModelForm()
    return render(
        request=request,
        template_name='register_contact.html',
        context={ 'new_contact_form':new_contact_form }
    )


def new_formofpay_view(request):
    if request.method == 'POST':
        new_formofpay_form = FormOfPaymentModelForm(request.POST)
        if new_formofpay_form.is_valid():
            new_formofpay_form.save()
            return('')  # colocar um redirect
    else:
        new_formofpay_form = FormOfPaymentModelForm()
    return render(
        request=request,
        template_name='register_form_payment.html',
        context={ 'new_formofpay_form':new_formofpay_form }
    )
