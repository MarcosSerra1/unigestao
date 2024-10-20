from django.urls import path
from employees.views import HomeView, EmployeesListView, EmployeesDetailView, CreateEmployeeView, UpdateEmployeeView, DeleteEmployeeView, UpdateContactView, UpdateAddressView, UpdateFormOfPayView, CreateOfficeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('employee/', EmployeesListView.as_view(), name='employee'),  # listagem de funcionários
    path('employee/<int:pk>/', EmployeesDetailView.as_view(), name='employee_details'),  # caminho para abrir detalhes sobre o funcionario 
    path('register-employee/', CreateEmployeeView.as_view(), name='register_employee'),  # registrar funcionário
    path('update-employee/<int:pk>/update/', UpdateEmployeeView.as_view(), name='update_employee'),  # atualizar funcionário
    path('update-contact/<int:pk>/update/', UpdateContactView.as_view(), name='update_contact'),  # atualizar contato
    path('update-address/<int:pk>/update/', UpdateAddressView.as_view(), name='update_address'),  # atualizar endereço
    path('update-form_of_payment/<int:pk>/update/', UpdateFormOfPayView.as_view(), name='update_form_of_payment'),  # atualizar forma de pagamento
    path('delete-employee/<int:pk>/delete/', DeleteEmployeeView.as_view(), name='delete_employee'),  # deletar funcionário
    path('create-office/', CreateOfficeView.as_view(), name='create_office'),  # criar um novo cargo
]
