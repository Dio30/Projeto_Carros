from django.contrib import admin
from .models import Carros

class CarrosAdmin(admin.ModelAdmin):
    list_display = ['nome_do_carro', 'marcas_de_carros', 'ano_de_fabricacao', 'ano_do_modelo', 
    'valor_do_carro', 'modelos_de_carros', 'motorizacao','fotos_de_carros', 'usuario']
    
admin.site.register(Carros, CarrosAdmin)