from django.views.generic.edit import  DeleteView   ##### views para Delete
from carrosselApp.models import *
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

class SetorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):

    login_url = reverse_lazy('login')
    group_required = u"admiistrador"
    model = Setor
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listSetor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluindo Setor"

        return context

class GradeDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Grade
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listGrade')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluindo Grade"

        return context

class ConteudoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Conteudo
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listConteudo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluindo Conteúdo"
        
        return context



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