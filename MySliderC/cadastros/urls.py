from django.urls import path

from .views import *

urlpatterns = [
    path('setor/',SetorCreate.as_view(), name='cadastrar-setor'),
    path('grade/',GradeCreate.as_view(), name='cadastrar-grade'),
    path('perfil/',PerfilCreate.as_view(), name='cadastrar-perfil'),
    path('usuario/',UsuarioCreate.as_view(), name='cadastrar-usuario'),
    path('perfil-usuario/',Perfil_UsuarioCreate.as_view(), name='cadastrar-perfil-usuario'),
    path('conteudo/',ConteudoCreate.as_view(), name='cadastrar-conteudo'),
 
]