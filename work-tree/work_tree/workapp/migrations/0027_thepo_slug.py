# Generated by Django 3.2.9 on 2021-11-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0026_auto_20211126_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='thepo',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]