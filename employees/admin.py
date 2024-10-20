from django.contrib import admin
from employees.models import Employee, Sex, EmployeeStatus, Office, ContactInfo, Address, TypePix, Bank, FormOfPayment, EmployeeInventory


class SexAdm(admin.ModelAdmin):
    list_display = ('sex',)
    search_fields = ('sex',)


class EmployeeStatusAdm(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)


class OfficeAdm(admin.ModelAdmin):
    list_display = ('office',)
    search_fields = ('office',)


class EmployeeAdm(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'birth_date', 'sex', 'email', 'name_mother', 'admission_date')
    search_fields = ('name',)


class ContactAdm(admin.ModelAdmin):
    list_display = ('employee', 'phone_number', 'emergency_contact_name', 'emergency_contact_number')
    search_fields = ('employee', 'phone_number')


class AddressAdm(admin.ModelAdmin):
    list_display = ('employee', 'postal_code', 'street', 'neighborhood', 'city',  'state', 'number',)
    search_fields = ('employee',)


class TypePixAdm(admin.ModelAdmin):
    list_display = ('type_pix',)
    search_fields = ('type_pix',)


class BankAdm(admin.ModelAdmin):
    list_display = ('bank',)
    search_fields = ('bank',)


class FormOfPaymentAdm(admin.ModelAdmin):
    list_display = ('employee', 'pix', 'bank', 'type_pix')
    search_fields = ('employee',)


class EmployeeInventoryAdm(admin.ModelAdmin):
    list_display = ('employee_count',)
    search_fields = ('employee_count',)


admin.site.register(Sex, SexAdm)
admin.site.register(EmployeeStatus, EmployeeStatusAdm)
admin.site.register(Office, OfficeAdm)
admin.site.register(Employee, EmployeeAdm)
admin.site.register(ContactInfo, ContactAdm)
admin.site.register(Address, AddressAdm)
admin.site.register(TypePix, TypePixAdm)
admin.site.register(Bank, BankAdm)
admin.site.register(FormOfPayment, FormOfPaymentAdm)
admin.site.register(EmployeeInventory, EmployeeInventoryAdm)
