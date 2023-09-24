from django.urls import path
### importando views para create
from .views import *
### importando views de update
from .upviews import *
### importando views de delete
from .deleteviews import *




urlpatterns = [
    #### urls para create ####
    path('setor/',SetorCreate.as_view(), name='cadastrar-setor'),
    path('grade/',GradeCreate.as_view(), name='cadastrar-grade'),
    path('perfil/',PerfilCreate.as_view(), name='cadastrar-perfil'),
    path('usuario/',UsuarioCreate.as_view(), name='cadastrar-usuario'),
    path('perfil-usuario/',Perfil_UsuarioCreate.as_view(), name='cadastrar-perfil-usuario'),
    path('conteudo/',ConteudoCreate.as_view(), name='cadastrar-conteudo'),
 

 #### urls para update ####

    path('editar/setor/<int:pk>/', SetorUpdate.as_view(), name='upSetor'),
    path('editar/grade/<int:pk>/', GradeUpdate.as_view(), name='upGrade'),
    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name='upPerfil'),
    path('editar/usuario/<int:pk>/', UsuarioUpdate.as_view(), name='upUsuario'),
    path('editar/perfil-usuario/<int:pk>/', Perfil_UsuarioUpdate.as_view(), name='upUsuarioPerfil'),
    path('editar/conteudo/<int:pk>/', ConteudoUpdate.as_view(), name='upConteudo'),

 #### urls para delete ####

    path('excluir/setor/<int:pk>/', SetorDelete.as_view(), name='delSetor'),
    path('excluir/grade/<int:pk>/', GradeDelete.as_view(), name='delGrade'),
    path('excluir/perfil/<int:pk>/', PerfilDelete.as_view(), name='delPerfil'),
    path('excluir/usuario/<int:pk>/', UsuarioDelete.as_view(), name='delUsuario'),
    path('excluir/perfil-usuario/<int:pk>/', Perfil_UsuarioDelete.as_view(), name='delUsuarioPerfil'),
    path('excluir/conteudo/<int:pk>/', ConteudoDelete.as_view(), name='delConteudo'),
]