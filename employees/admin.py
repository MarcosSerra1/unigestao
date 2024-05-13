from django.contrib import admin
from employees.models import Person, Sex, ContactInfo, Address, TypePix, Bank, FormOfPayment


class SexAdm(admin.ModelAdmin):
    list_display = ('sex',)
    search_fields = ('sex',)


class PersonAdm(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'birth_date', 'sex', 'email', 'name_mother')
    search_fields = ('name',)


class ContactAdm(admin.ModelAdmin):
    list_display = ('employee', 'phone_number', 'emergency_contact_name', 'emergency_contact_number')
    search_fields = ('employee', 'phone_number')


class AddressAdm(admin.ModelAdmin):
    list_display = ('employee', 'street', 'number', 'city', 'state', 'postal_code')
    search_fields = ('employee',)


class TypePixAdm(admin.ModelAdmin):
    list_display = ('type_pix',)
    search_fields = ('type_pix',)


class BankAdm(admin.ModelAdmin):
    list_display = ('bank',)
    search_fields = ('bank',)


class FormOfPaymentAdm(admin.ModelAdmin):
    list_display = ('employee', 'pix', 'bank', 'type_pix', 'recipient_name',)
    search_fields = ('employee',)


admin.site.register(Sex, SexAdm)
admin.site.register(Person, PersonAdm)
admin.site.register(ContactInfo, ContactAdm)
admin.site.register(Address, AddressAdm)
admin.site.register(TypePix, TypePixAdm)
admin.site.register(Bank, BankAdm)
admin.site.register(FormOfPayment, FormOfPaymentAdm)
