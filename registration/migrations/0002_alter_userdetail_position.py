# Generated by Django 3.2.4 on 2021-09-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='position',
            field=models.CharField(choices=[('0', 'プレイヤー'), ('1', 'マネージャー'), ('2', 'コーチ'), ('3', 'OB')], default='0', max_length=6),
        ),
    ]
