from django.db import models


class Sex(models.Model):
    sex = models.CharField(max_length=9)

    def __str__(self) -> str:
        return self.sex


class EmployeeStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.status


class Person(models.Model):
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    name_mother = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.PROTECT, related_name='person_sex')
    email = models.EmailField(blank=True, null=True)
    status = models.ForeignKey(EmployeeStatus, on_delete=models.PROTECT, related_name='employee_status', default=1)  # 1 represents "Ativo"

    def __str__(self) -> str:
        return self.name


class ContactInfo(models.Model):
    employee = models.OneToOneField(Person, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_number = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f'Contact for {self.employee.name}'


class Address(models.Model):
    employee = models.OneToOneField(Person, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'Address for {self.employee.name}'


class TypePix(models.Model):
    type_pix = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.type_pix


class Bank(models.Model):
    bank = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.bank


class FormOfPayment(models.Model):
    employee = models.OneToOneField(Person, on_delete=models.CASCADE)
    pix = models.CharField(max_length=50, blank=True, null=True)
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, related_name='bank_pix')
    type_pix = models.ForeignKey(TypePix, on_delete=models.PROTECT, related_name='pix')

    def __str__(self) -> str:
        return f'Pix for {self.employee.name}'
