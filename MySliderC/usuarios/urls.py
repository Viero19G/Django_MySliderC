from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views.views import *
from usuarios.views.upviews import *



urlpatterns = [
    # path('', view , name),
    path('entrar/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'
        ), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizarDados/', PerfilUpdate.as_view(), name='upPerfil')

]