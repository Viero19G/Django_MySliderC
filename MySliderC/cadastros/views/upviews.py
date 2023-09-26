from django.views.generic.edit import UpdateView
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.http import HttpResponseForbidden

class SetorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"marketing", u"administrador"]
    model = Setor
    fields = ['grade', 'nome']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listSetor')

    def dispatch(self, request, *args, **kwargs):
        # Obtenha o objeto Setor que deseja atualizar
        setor = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Setor
        if setor.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            # Redirecione para alguma página de erro ou exiba uma mensagem de erro
            return HttpResponseForbidden("Você não tem permissão para editar este Setor.")

class GradeUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u"marketing", u"administrador"]
    model = Grade
    fields = [ 'title','sub_title', 'conteudo']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listGrade')

    def dispatch(self, request, *args, **kwargs):
        # Obtenha o objeto Grade que deseja atualizar
        grade = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou a Grade
        if grade.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            # Redirecione para alguma página de erro ou exiba uma mensagem de erro
            return HttpResponseForbidden("Você não tem permissão para editar esta Grade.")

class ConteudoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Conteudo
    fields = [ 'title','sub_title','descricao','tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

    def dispatch(self, request, *args, **kwargs):
        # Obtenha o objeto Conteúdo que deseja atualizar
        conteudo = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Conteúdo
        if conteudo.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            # Redirecione para alguma página de erro ou exiba uma mensagem de erro
            return HttpResponseForbidden("Você não tem permissão para editar este Conteúdo.")


# class UsuarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
#     login_url = reverse_lazy('login')
#     model = Usuario
#     fields = [ 'usrNome','usrSenha', 'usrMail']
#     template_name = 'cadastros/create.html'
#     success_url = reverse_lazy('listUsuario')

# class PerfilUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
#     login_url = reverse_lazy('login')
#     group_required =  u"administrador"
#     model = Perfil
#     fields = [ 'perfilNome','descricao',]
#     template_name = 'cadastros/create.html'
#     success_url = reverse_lazy('listPerfil')

# class Perfil_UsuarioUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
#     login_url = reverse_lazy('login')
#     group_required =  u"administrador"
#     model = Perfil_Usuario
#     fields = [ 'descricao','usuario','perfil']
#     template_name = 'cadastros/create.html'
#     success_url = reverse_lazy('listUsuarioPerfil')