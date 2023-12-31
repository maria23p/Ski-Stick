# Generated by Django 4.2.6 on 2023-11-09 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSki', '0012_remove_servicio_costo_remove_servicio_horario_fin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Image'),
        ),
    ]
