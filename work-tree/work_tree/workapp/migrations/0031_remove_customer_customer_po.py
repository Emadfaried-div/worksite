# Generated by Django 3.2.9 on 2021-11-26 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0030_customer_customer_po'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_po',
        ),
    ]