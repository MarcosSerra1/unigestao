from django.urls import path
from employees.views import HomeView, EmployeesListView, EmployeesDetailView, new_person_view, new_address_view, new_contact_view, new_formofpay_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('employee/', EmployeesListView.as_view(), name='employee'),  # listagem de funcionários
    path('employee/<int:pk>/', EmployeesDetailView.as_view(), name='employee_details'),  # caminho para abrir detalhes sobre o funcionario 
    path('register/', new_person_view, name='register_person'),  # registrar funcionário
    path('address/', new_address_view, name='register_address'),  # registrar endereço
    path('contact/', new_contact_view, name='register_contact'),  # registrar contato
    path('form_of_pay/', new_formofpay_view, name='register_formofpayment'), # registrar forma de pagemnto
]
