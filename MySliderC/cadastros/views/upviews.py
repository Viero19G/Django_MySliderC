from django.views.generic.edit import UpdateView   ##### views para update
from carrosselApp.models import *
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class SetorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Setor
    fields = ['grade', 'nome']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listSetor')

class GradeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Grade
    fields = [ 'title','sub_title', 'conteudo']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listGrade')

class ConteudoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Conteudo
    fields = [ 'title','sub_title','descricao','tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Usuario
    fields = [ 'usrNome','usrSenha', 'usrMail']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listUsuario')

class PerfilUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = [ 'perfilNome','descricao',]
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listPerfil')

class Perfil_UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Perfil_Usuario
    fields = [ 'descricao','usuario','perfil']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listUsuarioPerfil')