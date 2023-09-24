from django.views.generic.edit import DeleteView   ##### views para Delete
from carrosselApp.models import *
from django.urls import reverse_lazy

class SetorDelete(DeleteView):
    model = Setor
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('inicio')

class GradeDelete(DeleteView):
    model = Grade
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('inicio')

class ConteudoDelete(DeleteView):
    model = Conteudo
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('inicio')

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('inicio')

class PerfilDelete(DeleteView):
    model = Perfil
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('inicio')

class Perfil_UsuarioDelete(DeleteView):
    model = Perfil_Usuario
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('inicio')