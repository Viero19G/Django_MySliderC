from django.views.generic.edit import  DeleteView   ##### views para Delete
from carrosselApp.models import *
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

class SetorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Setor
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listSetor')

class GradeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Grade
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listGrade')

class ConteudoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Conteudo
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listConteudo')

# class UsuarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
#     login_url = reverse_lazy('login')
#     group_required = u"admin"
#     model = Usuario
#     template_name = 'cadastros/delete.html'
#     success_url = reverse_lazy('listUsuario')

# class PerfilDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
#     login_url = reverse_lazy('login')
#     group_required = u"admin"
#     model = Perfil
#     template_name = 'cadastros/delete.html'
#     success_url = reverse_lazy('listPerfil')

# class Perfil_UsuarioDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
#     login_url = reverse_lazy('login')
#     group_required = u"admin"
#     model = Perfil_Usuario
#     template_name = 'cadastros/delete.html'
#     success_url = reverse_lazy('listUsuarioPerfil')