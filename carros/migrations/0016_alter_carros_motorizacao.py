# Generated by Django 4.0.5 on 2022-07-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0015_carros_motorizacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='motorizacao',
            field=models.TextField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=5, verbose_name='Turbo:'),
        ),
    ]
