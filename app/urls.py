from django.contrib import admin
from django.urls import path
from employees.views import home_view, new_person_view, list_persons_view, new_address_view, new_contact_view, new_formofpay_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('employee', list_persons_view, name='employee'),
    path('register/', new_person_view, name='register_person'),
    path('register/address/', new_address_view, name='register_address'),
    path('register/contact/', new_contact_view, name='register_contact'),
    path('register/form_of_pay/', new_formofpay_view, name='register_formofpayment'),
]
