from django.shortcuts import get_object_or_404, render, redirect
from .models import Carros
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView

class CarrosList(LoginRequiredMixin, ListView): # para listar os itens
    model = Carros
    queryset = Carros.objects.order_by('nome_do_carro').all()
    login_url = reverse_lazy('login')
    paginate_by = 3
    
    def get_queryset(self): # para cada usuario ser unico e não ter acesso a qualquer coisa de outros usuarios cadastrados
        self.object_list = Carros.objects.filter(usuario=self.request.user)
        return self.object_list
    
    def get(self, request, *args, **kwargs): #para pesquisar pelo nome do carro
        pesquisar = self.request.GET.get('nome_do_carro')
        if pesquisar:
            self.object_list = self.get_queryset().filter(nome_do_carro__icontains=pesquisar)
        else:
            self.object_list = self.get_queryset()
            
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)
    
class CarrosDetail(LoginRequiredMixin, DetailView): # para mostrar os itens em detalhes
    queryset = Carros.objects.all()
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Carros, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
class CarrosNew(LoginRequiredMixin, SuccessMessageMixin, CreateView): # para criar itens novos
    model = Carros
    fields = ['nome_do_carro', 'ano_de_fabricacao', 'ano_do_modelo', 'marcas_de_carros', 'valor_do_carro', 'modelos_de_carros', 'motorizacao','fotos_de_carros']
    success_url = reverse_lazy('lista')
    success_message = 'Carro adicionado com sucesso'
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Carros"
        return context
    
class CarrosUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView): # para editar os itens
    model = Carros
    fields = ['nome_do_carro', 'ano_de_fabricacao', 'ano_do_modelo', 'marcas_de_carros', 'valor_do_carro', 'modelos_de_carros', 'motorizacao','fotos_de_carros']
    success_url = reverse_lazy('lista')
    success_message = 'Carro atualizado com sucesso'
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Carros, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Carros"
        return context

class CarrosDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView): # para deletar os itens
    queryset = Carros.objects.all()
    success_url = reverse_lazy('lista')
    success_message = 'Carro foi deletado com sucesso'
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        self.object = get_object_or_404(Carros, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class ChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView): #caso queria alterar a sua senha
    template_name = 'registration/change_password.html'
    success_message = "Senha alterada com sucesso"
    success_url = reverse_lazy('lista')
    login_url = reverse_lazy('login') # se alguem tentar entrar em alguma pagina sem estar autenticado será redirecionado para o login

@login_required(login_url ='login')
def perfil(request): # onde é possivel alterar o usuario e adicionar/editar o email
    if request.method == "GET":
        return render(request, 'carros/perfil.html')
    
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        usuario = User.objects.filter(username=username).exclude(id=request.user.id)
        
        if usuario.exists():
            messages.error(request, "Já existe um usuario com esse nome")
            return render(request, template_name='carros/perfil.html')
        
        meu_email = User.objects.filter(email=email).exclude(id=request.user.id)
        
        if meu_email.exists():
            messages.error(request, "Já existe um usuario com esse email")
            return render(request, template_name='carros/perfil.html')
        
        request.user.username = username
        request.user.email = email
        request.user.save()
        messages.success(request, "Dados alterados com sucesso")
       
    return redirect('lista')