# Generated by Django 4.0.5 on 2022-06-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0004_alter_carros_valor_do_carro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='fotos_de_carros',
            field=models.ImageField(blank=True, null=True, upload_to='clients_photos', verbose_name='fotos'),
        ),
    ]