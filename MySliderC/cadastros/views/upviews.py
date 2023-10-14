from django.views.generic.edit import UpdateView
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import user_passes_test



# Função de verificação para permitir apenas superusuários
def is_superuser(user):
    return user.is_superuser


class SetorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Setor
    fields = ['nome', 'membros']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listSetor')

    def dispatch(self, request, *args, **kwargs):
        setor = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Setor
        if setor.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Você não tem permissão para editar este Setor.")
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Setor"
        context['botao'] = "Salvar"
        return context

class GradeUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Grade
    fields = [ 'title','sub_title', 'conteudo','setor']
    template_name = 'editar/upGrade.html'
    success_url = reverse_lazy('listGrade')

    def dispatch(self, request, *args, **kwargs):
        grade = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou a Grade
        if grade.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Você não tem permissão para editar esta Grade.")
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Grade"
        context['botao'] = "Salvar"
        return context

class ConteudoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Conteudo
    fields = [ 'title','sub_title','descricao','tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

    def dispatch(self, request, *args, **kwargs):
        conteudo = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Conteúdo
        if conteudo.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Você não tem permissão para editar este Conteúdo.")
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Conteúdo"
        context['botao'] = "Salvar"
        return context

class VideoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Video
    fields = [ 'video','title','sub_title','descricao']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

    def dispatch(self, request, *args, **kwargs):
        conteudo = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Conteúdo
        if conteudo.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Você não tem permissão para editar este Conteúdo.")
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Video"
        context['botao'] = "Salvar"
        return context


class ImagemUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Imagem
    fields = [ 'title','sub_title','descricao','tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

    def dispatch(self, request, *args, **kwargs):
        conteudo = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Conteúdo
        if conteudo.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Você não tem permissão para editar este Conteúdo.")
        
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Conteúdo"
        context['botao'] = "Salvar"
        return context
    

@user_passes_test(is_superuser)
class EditarGrupoView(UpdateView):
    model = Group
    template_name = "cadastros/editGroup.html"
    success_url = reverse_lazy('listGroups')
    fields = ['name']  # Adicione outros campos do grupo, se necessário

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        users = self.request.POST.getlist('users')
        grupo = form.save()
        grupo.user_set.set(users)  # Define a lista de usuários para o grupo
        return super().form_valid(form)