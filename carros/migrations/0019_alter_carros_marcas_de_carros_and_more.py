# Generated by Django 4.0.5 on 2022-07-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0018_alter_carros_motorizacao_alter_carros_valor_do_carro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='marcas_de_carros',
            field=models.CharField(choices=[('Citroen', 'Citroen'), ('Chevrolet', 'Chevrolet'), ('Ferrari', 'Ferrari'), ('Fiat', 'Fiat'), ('Ford', 'Ford'), ('Hyundai', 'Hyundai'), ('Jeep', 'Jeep'), ('Mercedes Benz', 'Mercedes Benz'), ('Peugeot', 'Peugeot'), ('Outros', 'Outros'), ('Renault', 'Renault'), ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen')], default='Outros', max_length=30, verbose_name='Fabricante:'),
        ),
        migrations.AlterField(
            model_name='carros',
            name='motorizacao',
            field=models.TextField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', help_text='O carro tem motorização turbo?', verbose_name='Turbo:'),
        ),
        migrations.AlterField(
            model_name='carros',
            name='valor_do_carro',
            field=models.CharField(choices=[('Entre R$ 0 e R$ 40.000,00', 'Entre R$ 0 e R$ 40.000,00'), ('Entre R$ 40.000,01 e R$ 80.000,00', 'Entre R$ 40.000,01 e R$ 80.000,00'), ('Entre R$ 80.000,01 e R$ 120.000,00', 'Entre R$ 80.000,01 e R$120.000,00'), ('Entre R$ 120.000,01 e R$ 240.000,00', 'Entre R$ 120.000,01 e R$ 240.000,00'), ('Entre R$ 240.000,01 e R$ 480.000,00', 'Entre R$ 240.000,01 e R$ 480.000,00'), ('Entre R$ 480.000,01 e R$ 960.000,00', 'Entre R$ 480.000,01 e R$ 960.000,00'), ('Não sabe informar', 'Não sabe informar')], default='Não sabe informar', max_length=50, verbose_name='Valor do Carro:'),
        ),
    ]
