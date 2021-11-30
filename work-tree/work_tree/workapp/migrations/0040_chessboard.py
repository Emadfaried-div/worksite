# Generated by Django 3.2.9 on 2021-11-28 21:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0039_alter_dailynotes_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChessBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8), size=8)),
            ],
        ),
    ]