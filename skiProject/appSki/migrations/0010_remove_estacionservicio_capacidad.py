# Generated by Django 4.2.6 on 2023-11-08 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appSki', '0009_estacionservicio_horario_fin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacionservicio',
            name='capacidad',
        ),
    ]