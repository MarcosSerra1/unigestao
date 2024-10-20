from django import forms
from employees.models import Employee, Address, ContactInfo, FormOfPayment, Office
from utils.validate_cpf import validar_cpf
from utils.replace_special_characters import substituir_caracteres_especiais


# Form Profissão
class OfficeModelForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = '__all__'


# Form Funcionario
class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = substituir_caracteres_especiais(name)
        return name
    
    def clean_name_mother(self):
        name_mother = self.cleaned_data.get('name_mother')
        name_mother = substituir_caracteres_especiais(name_mother)
        return name_mother

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        # Valida o formato do CPF e o CPF
        cpf = validar_cpf(cpf)

        if cpf is False:
            raise forms.ValidationError('CPF inválido')

        return cpf
    
    def save(self, commit=True):
        # Obtenha uma instância do objeto do modelo, mas não o salve ainda
        instance = super().save(commit=False)
        # Converte o nome para maiúsculas
        instance.name = instance.name.upper()
        # Converte o nome da mãe para maiúsculas
        instance.name_mother = instance.name_mother.upper()
        # Converte o e-mail para minúsculas
        instance.email = instance.email.lower()
        # Salva o objeto no banco de dados se commit for True
        if commit:
            instance.save()
        return instance


# Form Endereço
class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['postal_code', 'street', 'neighborhood', 'city',  'state', 'number',]

    def clean_street(self):
        street = self.cleaned_data.get('street')
        street = substituir_caracteres_especiais(street)
        return street

    def clean_neighborhood(self):
        neighborhood = self.cleaned_data.get('neighborhood')
        neighborhood = substituir_caracteres_especiais(neighborhood)
        return neighborhood
    
    def clean_city(self):
        city = self.cleaned_data.get('city')
        city = substituir_caracteres_especiais(city)
        return city
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.number = instance.number.upper()
        if commit:
            instance.save()
        return instance


# Form Contatos
class ContactInfoModelForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['phone_number', 'emergency_contact_name', 'emergency_contact_number']

    def clean_emergency_contact_name(self):
        emergency_contact_name = self.cleaned_data.get('emergency_contact_name')
        emergency_contact_name = substituir_caracteres_especiais(emergency_contact_name)
        return emergency_contact_name

    def save(self, commit=True):
        # Obtenha uma instância do objeto do modelo, mas não o salve ainda
        instance = super().save(commit=False)
        # Converte o nome do titular para maiúsculas
        instance.emergency_contact_name = instance.emergency_contact_name.upper()
        # Salva o objeto no banco de dados se commit for True
        if commit:
            instance.save()
        return instance


# Form Forma de pagamento
class FormOfPaymentModelForm(forms.ModelForm):
    class Meta:
        model = FormOfPayment
        fields = ['pix', 'bank', 'type_pix']
