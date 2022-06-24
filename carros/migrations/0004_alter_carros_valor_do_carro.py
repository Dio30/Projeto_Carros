# Generated by Django 4.0.5 on 2022-06-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0003_alter_carros_fotos_de_carros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='valor_do_carro',
            field=models.CharField(choices=[('Entre R$ 0 e R$ 40.000,00', 'Entre R$ 0 e R$ 40.000,00'), ('Entre R$ 40.000,01 e R$ 80.000,00', 'Entre R$ 40.000,01 e R$ 80.000,00'), ('Entre R$ 80.000,01 e R$ 120.000,00', 'Entre R$ 80.000,01 e R$120.000,00'), ('Entre R$ 120.000,01 e R$ 240.000,00', 'Entre R$ 120.000,01 e R$ 240.000,00'), ('Entre R$ 240.000,01 e R$ 480.000,00', 'Entre R$ 240.000,01 e R$ 480.000,00'), ('Entre R$ 480.000,01 e R$ 960.000,00', 'Entre R$ 480.000,01 e R$ 960.000,00'), ('Não sabe informar', 'Não sabe informar')], max_length=50),
        ),
    ]