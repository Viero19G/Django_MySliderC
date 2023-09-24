from django.views.generic.edit import UpdateView   ##### views para update
from carrosselApp.models import *
from django.urls import reverse_lazy

class SetorUpdate(UpdateView):
    model = Setor
    fields = ['grade', 'nome']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listSetor')

class GradeUpdate(UpdateView):
    model = Grade
    fields = [ 'title','sub_title', 'conteudo']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listGrade')

class ConteudoUpdate(UpdateView):
    model = Conteudo
    fields = [ 'title','sub_title','descricao','tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = [ 'usrNome','usrSenha', 'usrMail']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listUsuario')

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = [ 'perfilNome','descricao',]
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listPerfil')

class Perfil_UsuarioUpdate(UpdateView):
    model = Perfil_Usuario
    fields = [ 'descricao','usuario','perfil']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listUsuarioPerfil')