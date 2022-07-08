from django.db import models
from django.contrib.auth.models import User

carros_choice = (
    ('Citroen', 'Citroen'),
    ('Chevrolet', 'Chevrolet'),
    ('Ferrari', 'Ferrari'),
    ('Fiat', 'Fiat'),
    ('Ford', 'Ford'),
    ('Hyundai', 'Hyundai'),
    ('Jeep', 'Jeep'),
    ('Mercedes Benz', 'Mercedes Benz'),
    ('Peugeot', 'Peugeot'),
    ('Outros', 'Outros'),
    ('Renault', 'Renault'),
    ('Toyota', 'Toyota'),
    ('Volkswagen', 'Volkswagen'),
)

valor_carros = (
    ('Entre R$ 0 e R$ 40.000,00', 'Entre R$ 0 e R$ 40.000,00'),
    ('Entre R$ 40.000,01 e R$ 80.000,00', 'Entre R$ 40.000,01 e R$ 80.000,00'),
    ('Entre R$ 80.000,01 e R$ 120.000,00', 'Entre R$ 80.000,01 e R$120.000,00'),
    ('Entre R$ 120.000,01 e R$ 240.000,00', 'Entre R$ 120.000,01 e R$ 240.000,00'),
    ('Entre R$ 240.000,01 e R$ 480.000,00', 'Entre R$ 240.000,01 e R$ 480.000,00'),
    ('Entre R$ 480.000,01 e R$ 960.000,00', 'Entre R$ 480.000,01 e R$ 960.000,00'),
    ('Não sabe informar', 'Não sabe informar'),
)

motor_carros = (
    ('1.0', '1.0'),
    ('1.4', '1.4'),
    ('1.6', '1.6'),
    ('1.8', '1.8'),
    ('2.0', '2.0'),
    ('2.4', '2.4'),
    ('2.8', '2.8'),
    ('3.2', '3.2'),
    ('4.0', '4.0'),
)

motorizacao = (
    ('Sim', 'Sim'),
    ('Não', 'Não'),
)

ano_fabricacao = (
    ('Não sabe informar o ano de fabricação', 'Não sabe informar o ano de fabricação'),
    ('2022', '2022'),
    ('2021', '2021'),
    ('2020', '2020'),
    ('2019', '2019'),
    ('2018', '2018'),
    ('2017', '2017'),
    ('2016', '2016'),
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
    ('2009', '2009'),
    ('2008', '2008'),
    ('2007', '2007'),
    ('2006', '2006'),
    ('2005', '2005'),
    ('2004', '2004'),
    ('2003', '2003'),
    ('2002', '2002'),
    ('2001', '2001'),
    ('2000', '2000'),
    ('1999', '1999'),
    ('1998', '1998'),
    ('1997', '1997'),
    ('1996', '1996'),
    ('1995', '1995'),
    ('1994', '1994'),
    ('1993', '1993'),
    ('1992', '1992'),
    ('1991', '1991'),
    ('1990', '1990'),
)

ano_modelo = (
    ('Não sabe informar o ano do modelo', 'Não sabe informar o ano do modelo'),
    ('2023', '2023'),
    ('2022', '2022'),
    ('2021', '2021'),
    ('2020', '2020'),
    ('2019', '2019'),
    ('2018', '2018'),
    ('2017', '2017'),
    ('2016', '2016'),
    ('2015', '2015'),
    ('2014', '2014'),
    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
    ('2009', '2009'),
    ('2008', '2008'),
    ('2007', '2007'),
    ('2006', '2006'),
    ('2005', '2005'),
    ('2004', '2004'),
    ('2003', '2003'),
    ('2002', '2002'),
    ('2001', '2001'),
    ('2000', '2000'),
    ('1999', '1999'),
    ('1998', '1998'),
    ('1997', '1997'),
    ('1996', '1996'),
    ('1995', '1995'),
    ('1994', '1994'),
    ('1993', '1993'),
    ('1992', '1992'),
    ('1991', '1991'),
    ('1990', '1990'),
)

class Carros(models.Model): # modelo para o CRUD de carros
    nome_do_carro = models.CharField(max_length=30, verbose_name='Modelo do Carro:')
    ano_de_fabricacao = models.CharField(max_length=50, choices=ano_fabricacao, verbose_name='Ano de Fabricação:', default='Não sabe informar o ano de fabricação')
    ano_do_modelo = models.CharField(max_length=50, choices=ano_modelo, verbose_name='Ano do Modelo:', default='Não sabe informar o ano do modelo')
    marcas_de_carros = models.CharField(max_length=30, choices=carros_choice, verbose_name='Fabricante:', default='Outros')
    valor_do_carro = models.CharField(max_length=50, choices=valor_carros, verbose_name='Valor do Carro:', default='Não sabe informar')
    modelos_de_carros = models.CharField(max_length=30, choices=motor_carros, verbose_name='Motor:', default='1.0')
    fotos_de_carros = models.ImageField(upload_to='clients_photos', null=True, blank=True, verbose_name='Foto:')
    motorizacao = models.CharField(max_length=10, verbose_name='Turbo:', choices=motorizacao, default='Não', help_text='O carro tem motorização turbo?')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['nome_do_carro',]
    
    def __str__(self):
        return self.nome_do_carro
    
    @property
    def image_url(self):
        if self.fotos_de_carros and hasattr(self.fotos_de_carros, 'url'):
            return self.fotos_de_carros.url