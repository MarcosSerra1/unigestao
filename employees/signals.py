from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from employees.models import Person, EmployeeInventory

def employee_inventory_update():
    employee_count = Person.objects.all().count()
    EmployeeInventory.objects.create(
        employee_count = employee_count
    )

@receiver(post_save, sender=Person)
def employee_post_save(sender, instance, **kwargs):
    employee_inventory_update()

@receiver(post_delete, sender=Person)
def employee_post_delete(sender, instance, **kwargs):
    employee_inventory_update()
