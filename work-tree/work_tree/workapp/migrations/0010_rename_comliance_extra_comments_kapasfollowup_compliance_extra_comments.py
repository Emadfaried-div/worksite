# Generated by Django 3.2.9 on 2021-12-30 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0009_auto_20211230_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kapasfollowup',
            old_name='comliance_extra_comments',
            new_name='compliance_extra_comments',
        ),
    ]