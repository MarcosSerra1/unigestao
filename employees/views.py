from django.shortcuts import render, redirect, get_object_or_404
from employees.forms import PersonModelForm, AddressModelForm, ContactInfoModelForm, FormOfPaymentModelForm
from employees.models import Person

def home_view(request):
    return render(
        request=request,
        template_name='employees/home.html'
    )


def list_persons_view(request):
    persons = Person.objects.all().order_by('id')
    search = request.GET.get('search')

    if search:
        persons = Person.objects.filter(name__icontains=search)

    return render(
        request=request,
        template_name='employees/list_persons.html',
        context={ 'persons': persons })


# Define uma def de visualização para exibir os detalhes de um funcionário.
# Esta classe herda da classe DetailView do Django, que é uma visualização genérica para exibir os detalhes de um único objeto.
def employee_detail_view(request, pk):
    # Recupera o funcionário com base na chave primária (pk) fornecida.
    employee = get_object_or_404(Person, pk=pk)

    # Renderiza o template 'employee_details.html' com o contexto contendo o funcionário.
    return render(request, 'employees/employee_details.html', { 'employee': employee })




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
            return redirect('employees/register_formofpayment')
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
