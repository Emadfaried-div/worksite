# Generated by Django 3.2.9 on 2021-11-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0017_alter_monthmenets_monthtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailynotes',
            name='delete_obj',
            field=models.CharField(blank=True, choices=[('DONE', 'done'), ('NOT_YET', 'not-yet')], default='not-yet', max_length=100, null=True),
        ),
    ]
