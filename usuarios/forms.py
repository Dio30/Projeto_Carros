from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from django.core.exceptions import ValidationError

class UsuariosForm(UserCreationForm): # formulario para o cadastro de novos usuarios
    email = forms.EmailField(max_length=100, required=False, help_text="Insira um email valido, por exemplo: exemplo@exemplo.com")
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)    
    
    def clean_username(self):
        u = self.cleaned_data['username']
        if User.objects.filter(username=u).exists():
            raise ValidationError("O usuario {} já existe.".format(u))
        return u