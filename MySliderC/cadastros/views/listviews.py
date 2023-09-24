from django.views.generic.list import ListView   ##### views para listar
from carrosselApp.models import *
from django.urls import reverse_lazy

class SetorList(ListView):
    model = Setor
    template_name = 'cadastros/listas/setor.html'


class GradeList(ListView):
    model = Grade
    template_name = 'cadastros/listas/grade.html'

class ConteudoList(ListView):
    model = Conteudo
    template_name = 'cadastros/listas/conteudo.html'

class UsuarioList(ListView):
    model = Usuario
    template_name = 'cadastros/listas/usuario.html'

class PerfilList(ListView):
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'

class Perfil_UsuarioList(ListView):
    model = Perfil_Usuario
    template_name = 'cadastros/listas/perfilUsuario.html'