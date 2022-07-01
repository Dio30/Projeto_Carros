from django.urls import path
from .views import UsuarioCreate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastro/', UsuarioCreate.as_view(), name='cadastro'),
    path('', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm_view.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
]