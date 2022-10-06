from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from carros import urls as carros_urls
from usuarios import urls as usuarios_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carros/', include(carros_urls)),
    path('', include(usuarios_urls)),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # para visualizar arquivos de midia como imagens ou arquivos