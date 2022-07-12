from django import forms
from .models import Carros
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

motorizacao = [
    ('Sim', 'Sim'),
    ('Não', 'Não'),
]


class CarrosForm(forms.ModelForm): #se quiser alterar algo do model para cá basta apenas copiar o mesmo model para o forms
    motorizacao = forms.ChoiceField(label='O carro tem motorização Turbo?', initial='Não', widget=forms.RadioSelect, choices=motorizacao)
    
    class Meta:
        model = Carros
        fields = ('nome_do_carro', 'ano_de_fabricacao', 'ano_do_modelo', 'marcas_de_carros', 
                  'valor_do_carro', 'modelos_de_carros', 'motorizacao','fotos_de_carros')
        
class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    new_password2 =  forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")