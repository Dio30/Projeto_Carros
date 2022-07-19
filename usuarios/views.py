from django.urls import reverse_lazy
from .forms import UsuariosForm, UsuariosLoginForm
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

class UsuarioCreate(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    form_class = UsuariosForm
    success_message = "Usuário criado com sucesso"
    success_url = reverse_lazy('login')
    
class UsuarioLogIn(LoginView):
    form_class = UsuariosLoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('lista')
    redirect_field_name = 'next'