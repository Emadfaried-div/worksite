# Generated by Django 3.2.9 on 2021-11-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0023_theorder_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='theorder',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
