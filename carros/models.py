from django.db import models
from django.contrib.auth.models import User
from django.forms import Widget

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

class Carros(models.Model): # modelo para o CRUD de carros
    nome_do_carro = models.CharField(max_length=30, verbose_name='Modelo do Carro:')
    marcas_de_carros = models.CharField(max_length=30, choices=carros_choice, verbose_name='Fabricante:', default='Outros')
    valor_do_carro = models.CharField(max_length=50, choices=valor_carros, verbose_name='Valor do Carro:', default='Não sabe informar')
    modelos_de_carros = models.CharField(max_length=30, choices=motor_carros, verbose_name='Motor:', default='1.0')
    fotos_de_carros = models.ImageField(upload_to='clients_photos', null=True, blank=True, verbose_name='Foto:')
    motorizacao = models.TextField(choices=motorizacao, verbose_name='Turbo:', default='Não', help_text='O carro tem motorização turbo?')
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