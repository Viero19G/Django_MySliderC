from django.urls import path
from .views import PerfilForm, Perfil, create_view


urlpatterns = [
    path('inicio/', Perfil),
    path('PerfilForm/', PerfilForm),
   
   
]
