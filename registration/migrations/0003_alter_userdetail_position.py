# Generated by Django 3.2.4 on 2021-09-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_userdetail_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='position',
            field=models.CharField(max_length=6),
        ),
    ]
