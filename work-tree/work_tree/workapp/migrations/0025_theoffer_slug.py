# Generated by Django 3.2.9 on 2021-11-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0024_theorder_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='theoffer',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]