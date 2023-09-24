from django.views.generic.edit import CreateView
from carrosselApp.models import *
from django.urls import reverse_lazy

class SetorCreate(CreateView):
    model = Setor
    fields = ['grade', 'nome']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('inicio')

class GradeCreate(CreateView):
    model = Grade
    fields = [ 'title','sub_title', 'conteudo']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('inicio')

class ConteudoCreate(CreateView):
    model = Conteudo
    fields = [ 'title','sub_title','descricao','tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('inicio')

class UsuarioCreate(CreateView):
    model = Usuario
    fields = [ 'usrNome','usrSenha', 'usrMail']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('inicio')

class PerfilCreate(CreateView):
    model = Perfil
    fields = [ 'perfilNome','descricao',]
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('inicio')

class Perfil_UsuarioCreate(CreateView):
    model = Perfil_Usuario
    fields = [ 'descricao','usuario','perfil']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('inicio')