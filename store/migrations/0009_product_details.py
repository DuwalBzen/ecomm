# Generated by Django 3.0.3 on 2020-09-21 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20200922_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(blank=True),
        ),
    ]
