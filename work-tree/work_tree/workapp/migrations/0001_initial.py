# Generated by Django 3.2.9 on 2021-11-16 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('vendor', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('DONE', 'done'), ('NOT_YET', 'not-yet')], default='not-yet', max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TheOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('section', models.CharField(blank=True, choices=[('ELECTRICAL', 'electerical'), ('MECHANICAL', 'mechanical'), ('ELECTRICAL & MECHANICAL', 'electrical & mechanical')], default='mechanical', max_length=100, null=True)),
                ('market', models.CharField(blank=True, choices=[('LOCAL', 'Local'), ('EXTERNAL', 'External')], default='Local', max_length=200, null=True)),
                ('vendor', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('responseibilty', models.CharField(max_length=200)),
                ('image_of_offer', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image', models.ImageField(upload_to='products')),
                ('offer2_image2', models.ImageField(blank=True, null=True, upload_to='products')),
                ('offer3_image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('totalprice', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThePo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dept', models.CharField(blank=True, max_length=200, null=True)),
                ('section', models.CharField(blank=True, choices=[('ELECTRICAL', 'electerical'), ('MECHANICAL', 'mechanical'), ('ELECTRICAL & MECHANICAL', 'electrical & mechanical')], default='mechanical', max_length=100, null=True)),
                ('market', models.CharField(blank=True, choices=[('LOCAL', 'Local'), ('EXTERNAL', 'External')], default='Local', max_length=200, null=True)),
                ('vendor', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('responseibilty', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='products')),
                ('document', models.FileField(blank=True, null=True, upload_to='Order-doc/')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('samples', models.CharField(blank=True, max_length=200, null=True)),
                ('numbers_of_offers', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workapp.theoffer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TheOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dept', models.CharField(blank=True, max_length=200, null=True)),
                ('section', models.CharField(blank=True, choices=[('ELECTRICAL', 'electerical'), ('MECHANICAL', 'mechanical'), ('ELECTRICAL & MECHANICAL', 'electrical & mechanical')], default='mechanical', max_length=100, null=True)),
                ('market', models.CharField(blank=True, choices=[('LOCAL', 'Local'), ('EXTERNAL', 'External')], default='Local', max_length=200, null=True)),
                ('vendor', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('responseibilty', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='products')),
                ('document', models.FileField(blank=True, null=True, upload_to='Order-doc/')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('samples', models.CharField(blank=True, max_length=200, null=True)),
                ('numbers_of_offers', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('notes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workapp.dailynotes')),
                ('offer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workapp.theoffer')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True)),
                ('image', models.ImageField(upload_to='monthly_Report')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
