from django.urls import path
from employees.views import HomeView, EmployeesListView, EmployeesDetailView, CreateEmployeeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('employee/', EmployeesListView.as_view(), name='employee'),  # listagem de funcionários
    path('employee/<int:pk>/', EmployeesDetailView.as_view(), name='employee_details'),  # caminho para abrir detalhes sobre o funcionario 
    path('register-employee/', CreateEmployeeView.as_view(), name='register_employee'),  # registrar funcionário
]
