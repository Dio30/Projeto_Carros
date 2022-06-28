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
    ('4.0', '4.0'),
)

class Carros(models.Model): # meu modelo principal para o CRUD de carros
    nome_do_carro = models.CharField(max_length=30)
    marcas_de_carros = models.CharField(max_length=30, choices=carros_choice)
    valor_do_carro = models.CharField(max_length=50, choices=valor_carros)
    modelos_de_carros = models.CharField(max_length=30, choices=motor_carros, verbose_name='Motor')
    fotos_de_carros = models.ImageField(upload_to='clients_photos', null=True, blank=True, verbose_name='Foto:')
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