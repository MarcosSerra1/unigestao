from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from employees.models import Employee, EmployeeInventory

def employee_inventory_update():
    employee_count = Employee.objects.all().count()
    EmployeeInventory.objects.create(
        employee_count = employee_count
    )

@receiver(post_save, sender=Employee)
def employee_post_save(sender, instance, **kwargs):
    employee_inventory_update()

@receiver(post_delete, sender=Employee)
def employee_post_delete(sender, instance, **kwargs):
    employee_inventory_update()
