from django import forms
from employees.models import Person, Sex, Address, ContactInfo, FormOfPayment, Bank, TypePix
from utils.validate_cpf import validar_cpf
from utils.replace_special_characters import substituir_caracteres_especiais


# Form Funcionario
class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = substituir_caracteres_especiais(name)
        return name
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        # Valida o formato do CPF
        cpf = validar_cpf(cpf)

        if cpf is False:
            raise forms.ValidationError('CPF inválido')

        # Verifica se o CPF já existe no banco de dados
        if Person.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está cadastrado')

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
        fields = '__all__'

    employee = forms.ModelChoiceField(Person.objects.all(), label='Funcionários')
    postal_code = forms.CharField(label='CEP', max_length=20)
    street = forms.CharField(label='Rua', max_length=255)
    number = forms.CharField(label='Número', max_length=10)
    state = forms.CharField(label='Estado', max_length=2)
    city = forms.CharField(label='Cidade', max_length=100)


# Form Contatos
class ContactInfoModelForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'

    employee = forms.ModelChoiceField(Person.objects.all(), label='Funcionarios')
    phone_number = forms.CharField(label='Número de Telefone', max_length=15)
    emergency_contact_name = forms.CharField(label='Nome do Contato de Emergência', max_length=200)
    emergency_contact_number = forms.CharField(label='Número do Contato de Emergência', max_length=15)

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
        fields = '__all__'

    employee = forms.ModelChoiceField(Person.objects.all(), label='Funcionarios')
    pix = forms.CharField(label='Pix', max_length=50, required=False)
    bank = forms.ModelChoiceField(label='Banco', queryset=Bank.objects.all())
    type_pix = forms.ModelChoiceField(label='Tipo de Pix', queryset=TypePix.objects.all())
    recipient_name = forms.CharField(label='Nome do Titular', max_length=200, required=False)

    def save(self, commit=True):
        # Obtenha uma instância do objeto do modelo, mas não o salve ainda
        instance = super().save(commit=False)
        # Converte o nome do titular para maiúsculas
        instance.recipient_name = instance.recipient_name.upper()
        # Salva o objeto no banco de dados se commit for True
        if commit:
            instance.save()
        return instance
