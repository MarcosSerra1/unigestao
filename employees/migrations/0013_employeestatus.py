# Generated by Django 5.0.4 on 2024-05-30 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_person_name_mother'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]