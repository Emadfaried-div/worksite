# Generated by Django 3.2.9 on 2021-12-30 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0010_rename_comliance_extra_comments_kapasfollowup_compliance_extra_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kapasfollowup',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
