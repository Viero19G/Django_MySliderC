from django.views.generic.list import ListView   ##### views para listar
from carrosselApp.models import *
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class SetorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Setor
    template_name = 'cadastros/listas/setor.html'


class GradeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Grade
    template_name = 'cadastros/listas/grade.html'

class ConteudoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Conteudo
    template_name = 'cadastros/listas/conteudo.html'

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