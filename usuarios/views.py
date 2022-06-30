from django.shortcuts import render, redirect
from .forms import UsuariosForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def register(request): # formulario para cadastrar novos usuarios
    template_name= "register.html"
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f"Usuario cadastrado com sucesso com o nome de {username}")
            return redirect("login")
        else:
            messages.warning(request, "Erro ao cadastrar, tente novamente obedecendo as dicas abaixo.")
            return redirect("cadastro")
    else:
        form = UsuariosForm
        context= {"register_form":form}
        return render(request, template_name, context)
    
def login_request(request): # para poder fazer login com segurança
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
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
            messages.error(request, "Usuário ou senha inválidos, tente novamente")
            return redirect("login")
    else:
        form = AuthenticationForm()
        return render(request, template_name="registration/login.html", context={"login_form":form})
       
def logout_request(request): # para poder fazer logout com segurança
    logout(request)
    messages.success(request, "Voce deslogou com sucesso.")
    return redirect ('login')