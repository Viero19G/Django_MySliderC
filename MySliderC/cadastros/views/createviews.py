from django.views.generic.edit import CreateView
from carrosselApp.models import *
from django.urls import reverse_lazy

## import verificação de login
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

class SetorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')

    model = Setor
    fields = ['grade', 'nome']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listSetor')

class GradeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Grade
    fields = [ 'title','sub_title', 'conteudo']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listGrade')

class ConteudoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Conteudo
    fields = [ 'title','sub_title','descricao','tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

# class UsuarioCreate(LoginRequiredMixin, CreateView):
#     login_url = reverse_lazy('login')
#     model = Usuario
#     fields = [ 'usrNome','usrSenha', 'usrMail']
#     template_name = 'cadastros/create.html'
#     success_url = reverse_lazy('listUsuario')

# class PerfilCreate(LoginRequiredMixin, CreateView):
#     login_url = reverse_lazy('login')
#     model = Perfil
#     fields = [ 'perfilNome','descricao',]
#     template_name = 'cadastros/create.html'
#     success_url = reverse_lazy('listPerfil')

# class Perfil_UsuarioCreate(LoginRequiredMixin, CreateView):
#     login_url = reverse_lazy('login')
#     model = Perfil_Usuario
#     fields = [ 'descricao','usuario','perfil']
#     template_name = 'cadastros/create.html'
#     success_url = reverse_lazy('listUsuarioPerfil')