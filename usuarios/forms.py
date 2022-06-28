from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UsuariosForm(UserCreationForm): # formulario para o cadastro de novos usuarios
    class Meta:
        model = User
        fields = ("username", "password1", "password2")