# Generated by Django 4.0.5 on 2022-06-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0006_alter_carros_fotos_de_carros_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='fotos_de_carros',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos', verbose_name='Foto'),
        ),
    ]
