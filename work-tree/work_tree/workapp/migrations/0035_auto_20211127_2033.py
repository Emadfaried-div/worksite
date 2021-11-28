# Generated by Django 3.2.9 on 2021-11-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0034_alter_dailynotes_due_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('can_mark_returned', 'Set book as returned'),),
            },
        ),
        migrations.AlterModelOptions(
            name='dailynotes',
            options={'permissions': (('can_view_daily notes', 'can_view_month menets'),)},
        ),
    ]