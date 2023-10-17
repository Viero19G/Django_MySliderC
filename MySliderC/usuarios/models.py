from django.db import models
from django.contrib.auth.models import User
from social_django.models import UserSocialAuth  

class Perfil(models.Model):
    nome_completo= models.CharField(max_length=50, null=True, verbose_name='Nome Completo ')
    cpf = models.CharField(max_length=14, null=True, verbose_name='CPF ')
    telefone = models.CharField(max_length=16, null=True, verbose_name='Telefone ')
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário ')

      # Campo para associar a autenticação social com o Google
    social_auth = models.ForeignKey(UserSocialAuth, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Autenticação Social')