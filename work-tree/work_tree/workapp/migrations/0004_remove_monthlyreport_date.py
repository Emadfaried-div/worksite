# Generated by Django 3.2.9 on 2021-11-19 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0003_monthlyreport_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyreport',
            name='date',
        ),
    ]
