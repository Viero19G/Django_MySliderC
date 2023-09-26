from django.views.generic.list import ListView   ##### views para listar
from carrosselApp.models import *
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class SetorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Setor
    template_name = 'cadastros/listas/setor.html'

    def get_queryset(self):
        user = self.request.user
        # Verifique se o usuário não é membro do grupo admin
        if not user.groups.filter(name='admin').exists():
            # Se não for membro do grupo admin, filtre os conteúdos pelo usuário
            queryset = Setor.objects.filter(usuario=user)
        else:
            # Se for membro do grupo admin, retorne todos os conteúdos
            queryset = Setor.objects.all()
        return queryset

class GradeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Grade
    template_name = 'cadastros/listas/grade.html'

    def get_queryset(self):
        user = self.request.user
        # Verifique se o usuário não é membro do grupo admin
        if not user.groups.filter(name='admin').exists():
            # Se não for membro do grupo admin, filtre os conteúdos pelo usuário
            queryset = Grade.objects.filter(usuario=user)
        else:
            # Se for membro do grupo admin, retorne todos os conteúdos
            queryset = Grade.objects.all()
        return queryset


class ConteudoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Conteudo
    template_name = 'cadastros/listas/conteudo.html'

    def get_queryset(self):
        user = self.request.user
        # Verifique se o usuário não é membro do grupo admin
        if not user.groups.filter(name='admin').exists():
            # Se não for membro do grupo admin, filtre os conteúdos pelo usuário
            queryset = Conteudo.objects.filter(usuario=user)
        else:
            # Se for membro do grupo admin, retorne todos os conteúdos
            queryset = Conteudo.objects.all()
        return queryset


# class UsuarioList(LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     model = Usuario
#     template_name = 'cadastros/listas/usuario.html'

# class PerfilList(LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     model = Perfil
#     template_name = 'cadastros/listas/perfil.html'

# class Perfil_UsuarioList(LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     model = Perfil_Usuario
#     template_name = 'cadastros/listas/perfilUsuario.html'