# Generated by Django 4.1 on 2022-09-28 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_alter_citas_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='fecha',
            field=models.DateTimeField(verbose_name='Fecha'),
        ),
    ]
