# Generated by Django 3.0.3 on 2020-09-21 21:05

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20200922_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=14, region=None),
        ),
    ]
