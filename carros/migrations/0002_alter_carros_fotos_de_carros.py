# Generated by Django 4.0.5 on 2022-06-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='fotos_de_carros',
            field=models.ImageField(blank=True, default='/static/imagens/carro padrão.png', null=True, upload_to='clients_photos'),
        ),
    ]
