# Generated by Django 4.2.6 on 2023-11-08 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSki', '0005_alter_estacion_superficie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estacion',
            old_name='horario',
            new_name='horario_fin',
        ),
        migrations.RenameField(
            model_name='servicio',
            old_name='horario',
            new_name='horario_fin',
        ),
        migrations.AddField(
            model_name='estacion',
            name='horario_ini',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='horario_ini',
            field=models.TimeField(default='00:00:00'),
        ),
    ]