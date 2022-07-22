from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class UsuariosForm(UserCreationForm):# formulario para o cadastro de novos usuarios
    username = forms.CharField(min_length=3, required=True, label='Usuário')
    email = forms.EmailField(min_length=11, required=False)
    
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
    
class UsuariosLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if username and password:
            if not user :
                raise forms.ValidationError('O usuário {} não existe'.format(username))
            if not user.check_password(password):
                raise forms.ValidationError('A senha está incorreta')
            if not user.is_active:
                raise forms.ValidationError('O usuário {} não está ativo.'.format(username))
        return super(UsuariosLoginForm, self).clean(*args, **kwargs)
    
    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user