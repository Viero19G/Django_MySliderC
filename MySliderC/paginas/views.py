from django.views.generic import TemplateView
from django.shortcuts import render
from carrosselApp.models import Setor, Grade
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user

        # Inicializar variáveis
        usuarios = None
        perfil = None
        grades_editadas = []
        grades_criadas = []
        setores_pertencentes = []

        # Verificar se o usuário tem um perfil
        if hasattr(usuario, 'perfil'):
            perfil = usuario.perfil

            # Buscar grades em que o usuário é editor
            grades_editadas = Grade.objects.filter(usuariosEdit=usuario)

            # Buscar grades que o usuário criou
            grades_criadas = Grade.objects.filter(usuario=usuario)

            # Buscar setores aos quais o usuário pertence
            setores_pertencentes = Setor.objects.filter(membros=usuario)
            

        # Se o perfil for None, obtenha todas as grades, usuários e setores
        else:
            grades_editadas = Grade.objects.all()
            grades_criadas = Grade.objects.all()
            setores_pertencentes = Setor.objects.all()
            usuarios = User.objects.all()

        context['perfil'] = perfil
        context['grades_editadas'] = grades_editadas
        context['grades_criadas'] = grades_criadas
        context['setores_pertencentes'] = setores_pertencentes
        context['usuarios'] = usuarios

        return context


@method_decorator(login_required, name='dispatch')
class MenuView(LoginRequiredMixin, TemplateView):
    template_name = 'paginas/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Adicionar lógica para verificar o tipo de usuário
        if user.is_superuser or user.groups.filter(name='administrador').exists():
            context['mensagem'] = f'Olá, {user.username}! Você possui permissões de administrador neste sistema.'
        elif user.groups.filter(name='marketing').exists():
            context['mensagem'] = f'Olá, {user.username}! Você possui permissões de marketing neste sistema.'
        else:
            context['mensagem'] = f'Olá, {user.username}!  Você possui permissões de usuário neste sistema.'

        # Adicionar lógica para obter setores
        context['setores'] = Setor.objects.all()

        # Adicionar lógica para obter grades e verificar permissões do usuário
        grades = Grade.objects.all()

        user_can_edit = (
            user.is_superuser
            or user.groups.filter(name='administrador').exists()
            or user.groups.filter(name='marketing').exists()
        )

        for grade in grades:
            grade.user_can_edit = user_can_edit or user in grade.usuariosEdit.all(
            ) or user.setor_set.filter(id__in=grade.setor.all()).exists()

        context['grades'] = grades

        return context
