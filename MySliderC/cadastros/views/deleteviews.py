from django.views.generic.edit import  DeleteView   ##### views para Delete
from carrosselApp.models import *
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class SetorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Setor
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listSetor')

class GradeDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Grade
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listGrade')

class ConteudoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Conteudo
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listConteudo')

class UsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Usuario
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listUsuario')

class PerfilDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listPerfil')

class Perfil_UsuarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Perfil_Usuario
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listUsuarioPerfil')