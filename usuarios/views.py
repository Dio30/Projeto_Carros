from django.shortcuts import render, redirect
from .forms import UsuariosForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def register_request(request):
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"Usuario cadastrado com sucesso por {username}")
            return redirect("login")
        else:
            messages.error(request, "Você não obedeceu algum dos criterios abaixo, tente novamente")
    else:
        form = UsuariosForm
        return render(request, template_name="register.html", context={"register_form":form})
    
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Você está logado como {username}.")
                return redirect("lista")
            else:
                return redirect("login")
        else:
            messages.error(request, "Usuario ou senha incorretos, tente novamente")
    
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})
    
def logout_request(request):
    logout(request)
    messages.success(request, "Voce deslogou com sucesso.")
    return redirect ('login')

class ChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_message = "Senha alterada com sucesso"
    success_url = reverse_lazy('lista')