from django.urls import path
from .views import CarrosList, CarrosNew, CarrosDetail, CarrosUpdate, CarrosDelete, perfil, ChangePasswordView

urlpatterns = [
    path('lista/', CarrosList.as_view(), name='lista'),
    path('novo/', CarrosNew.as_view(), name='novo'),
    path('detalhes/<int:pk>/', CarrosDetail.as_view(), name='detalhar'),
    path('editar/<int:pk>/', CarrosUpdate.as_view(), name='editar'),
    path('deletar/<int:pk>/', CarrosDelete.as_view(), name='deletar'),
    path('perfil/', perfil ,name='perfil'),
    path('alterar_senha/', ChangePasswordView.as_view(), name='password_change'),
]