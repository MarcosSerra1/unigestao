# Generated by Django 5.0.4 on 2024-06-03 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_person_admission_date_person_create_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='neighborhood',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]