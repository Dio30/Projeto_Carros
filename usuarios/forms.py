from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UsuariosForm(UserCreationForm):# formulario para o cadastro de novos usuarios
    username = forms.CharField(min_length=3, required=True, label='Usuário', 
            help_text='Obrigatório 3 caracteres ou mais. Letras, números e @/./+/-/_ apenas.')
    
    email = forms.EmailField(max_length=100, required=False, help_text="Insira um email valido, por exemplo: exemplo@exemplo.com")
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def clean_username(self):
        u = self.cleaned_data['username']
        if User.objects.filter(username=u).exists():
            raise ValidationError("O usuário {} já existe.".format(u))
        return u
    
    #def clean_email(self):
    #    e = self.cleaned_data['email']
    #    if User.objects.filter(email=e).exists():
    #        raise ValidationError("O email {} já existe.".format(e))
    #    return e