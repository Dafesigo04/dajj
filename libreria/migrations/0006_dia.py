# Generated by Django 4.1 on 2022-10-01 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0005_alter_citas_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombres')),
            ],
            options={
                'verbose_name': 'Dia',
                'verbose_name_plural': 'Dias',
                'db_table': 'dia',
                'ordering': ['id'],
            },
        ),
    ]
