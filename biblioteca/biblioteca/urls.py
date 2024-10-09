from django.contrib import admin
from django.urls import path, include
from core.views import HomeView  # Importe a view HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Usar HomeView como view baseada em classe
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Inclui as URLs do aplicativo core
]
