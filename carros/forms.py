from .models import Carros
from django import forms

class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Carros
        fields = ['fotos_de_carros']