# Generated by Django 4.1.7 on 2025-02-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_remove_appointment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='booked_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
