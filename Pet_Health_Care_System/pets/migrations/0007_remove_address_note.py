# Generated by Django 4.1.7 on 2025-02-22 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0006_remove_address_postal_code_address_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='note',
        ),
    ]
