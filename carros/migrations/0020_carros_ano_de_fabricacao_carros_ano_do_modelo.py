# Generated by Django 4.0.5 on 2022-07-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0019_alter_carros_marcas_de_carros_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carros',
            name='ano_de_fabricacao',
            field=models.CharField(choices=[('Não sabe informar o ano de fabricação', 'Não sabe informar o ano de fabricação'), ('Entre 1990 e 1995', 'Entre 1990 e 1995'), ('Entre 1996 e 2000', 'Entre 1996 e 2000'), ('Entre 2001 e 2005', 'Entre 2001 e 2005'), ('Entre 2006 e 2010', 'Entre 2006 e 2010'), ('Entre 2011 e 2015', 'Entre 2011 e 2015'), ('Entre 2016 e 2020', 'Entre 2016 e 2020'), ('Entre 2021 / atualmente', 'Entre 2021 / atualmente')], default='Não sabe informar o ano de fabricação', max_length=50, verbose_name='Ano de Fabricação'),
        ),
        migrations.AddField(
            model_name='carros',
            name='ano_do_modelo',
            field=models.CharField(choices=[('Não sabe informar o ano do modelo', 'Não sabe informar o ano do modelo'), ('Entre 1990 e 1995', 'Entre 1990 e 1995'), ('Entre 1996 e 2000', 'Entre 1996 e 2000'), ('Entre 2001 e 2005', 'Entre 2001 e 2005'), ('Entre 2006 e 2010', 'Entre 2006 e 2010'), ('Entre 2011 e 2015', 'Entre 2011 e 2015'), ('Entre 2016 e 2020', 'Entre 2016 e 2020'), ('Entre 2021 / atualmente', 'Entre 2021 / atualmente')], default='Não sabe informar o ano do modelo', max_length=50, verbose_name='Ano do Modelo'),
        ),
    ]
