# Generated by Django 4.2.6 on 2023-11-08 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appSki', '0011_servicio_costo_servicio_horario_fin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='costo',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='horario_fin',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='horario_ini',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='reserva',
        ),
    ]