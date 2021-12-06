# Generated by Django 3.2.9 on 2021-12-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0044_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theorder',
            name='dept',
        ),
        migrations.AddField(
            model_name='theorder',
            name='area',
            field=models.CharField(blank=True, choices=[('BM3', 'BM3'), ('BM4', 'BM4'), ('BM5', 'BM5'), ('BM6', 'BM6'), ('CAP_Inj Nessie1', 'CAP_Inj Nessie1'), ('CAP_Inj Nessie2', 'CAP_Inj Nessie2'), ('CAP_Inj Arburg', 'CAP_Inj Arburg'), ('CAP_assempl', 'CAP_assempl'), ('BP360AMP', 'BP360AMP'), ('BP360LV', 'BP360LV'), ('BP460', 'BP460'), ('BP312', 'BP312'), ('Micro-lab', 'Micro-lab'), ('Micro-Chimical', 'Micro-Chimical'), ('BM-Piovan', 'BM-Piovan')], default='?', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dailynotes',
            name='area',
            field=models.CharField(blank=True, choices=[('BM3', 'BM3'), ('BM4', 'BM4'), ('BM5', 'BM5'), ('BM6', 'BM6'), ('CAP_Inj Nessie1', 'CAP_Inj Nessie1'), ('CAP_Inj Nessie2', 'CAP_Inj Nessie2'), ('CAP_Inj Arburg', 'CAP_Inj Arburg'), ('CAP_assempl', 'CAP_assempl'), ('BP360AMP', 'BP360AMP'), ('BP360LV', 'BP360LV'), ('BP460', 'BP460'), ('BP312', 'BP312'), ('Micro-lab', 'Micro-lab'), ('Micro-Chimical', 'Micro-Chimical'), ('BM-Piovan', 'BM-Piovan')], default='?', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='monthmenets',
            name='area',
            field=models.CharField(blank=True, choices=[('BM3', 'BM3'), ('BM4', 'BM4'), ('BM5', 'BM5'), ('BM6', 'BM6'), ('CAP_Inj Nessie1', 'CAP_Inj Nessie1'), ('CAP_Inj Nessie2', 'CAP_Inj Nessie2'), ('CAP_Inj Arburg', 'CAP_Inj Arburg'), ('CAP_assempl', 'CAP_assempl'), ('BP360AMP', 'BP360AMP'), ('BP360LV', 'BP360LV'), ('BP460', 'BP460'), ('BP312', 'BP312'), ('Micro-lab', 'Micro-lab'), ('Micro-Chimical', 'Micro-Chimical'), ('BM-Piovan', 'BM-Piovan')], default='Bp360AMP', max_length=100, null=True),
        ),
    ]
