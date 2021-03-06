# Generated by Django 3.2.9 on 2022-01-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='calendar_id',
            new_name='calendar',
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('WR', 'work'), ('MT', 'maintenance'), ('od', 'audit')], default='MT', max_length=2),
        ),
    ]
