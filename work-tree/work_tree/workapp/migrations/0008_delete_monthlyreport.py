# Generated by Django 3.2.9 on 2021-11-21 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0007_remove_monthlyreport_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthlyReport',
        ),
    ]