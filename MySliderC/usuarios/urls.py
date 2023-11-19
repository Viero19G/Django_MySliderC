from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views.views import *
from usuarios.views.upviews import *
from usuarios.views.listviews import *
from usuarios.views.deleteviews import *
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuarios.views.authview import social_auth_google_redirect 
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('', view , name),
    path('entrar/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'
        ), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizarDados/', PerfilUpdate.as_view(), name='upPerfil'),
    path('verUsuarios/', UserListView.as_view(), name='verUsers'),

    path('users/edit/<int:pk>', UserEditView.as_view(), name='user_edit'),


 ##################################################################################################################
    path('auth/google/', auth_views.LoginView.as_view(), name='social_begin', kwargs={'backend': 'google-oauth2'}),
   #   interrompido    temporariamente
    path('auth/google/redirect/', social_auth_google_redirect, name='social_auth_google_redirect'),
    path('usuarios/auth/', include('social_django.urls', namespace='social')),
######################################################################################################################

    path('set-password/<int:user_id>/', CustomSetPasswordView.as_view(), name='user_pass'),
    path('usuarios/users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]