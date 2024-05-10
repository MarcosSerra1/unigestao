# Generated by Django 5.0.4 on 2024-05-08 01:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_bank'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormOfPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pix', models.CharField(blank=True, max_length=50, null=True)),
                ('recipient_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bank_pix', to='employees.bank')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employees.person')),
                ('type_pix', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pix', to='employees.typepix')),
            ],
        ),
    ]
