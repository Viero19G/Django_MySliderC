from django.views.generic.edit import CreateView
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.db.models import Q 
## import verificação de login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group 
from braces.views import GroupRequiredMixin

class SetorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Setor
    fields = ['nome', 'membros']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listSetor')
    
    def form_valid(self, form):
        user = self.request.user
        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, permita que ele crie o setor
            form.instance.usuario = user
            return super().form_valid(form)
        else:
            # Se o usuário não pertencer a nenhum desses grupos, não permita criar o setor
            return self.handle_no_permission()
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Setor"
        context['botao'] = "Cadastrar"
        return context

class GradeCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Grade
    fields = ['title', 'sub_title', 'conteudo', 'usuariosEdit', 'setor']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listGrade')
    
    def form_valid(self, form):
        user = self.request.user
        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, permita que ele crie a grade
            form.instance.usuario = user
            return super().form_valid(form)
        else:
            # Se o usuário não pertencer a nenhum desses grupos, não permita criar a grade
            return self.handle_no_permission()
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Grade"
        context['botao'] = "Cadastrar"
        return context

class ConteudoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Conteudo
    fields = ['title', 'sub_title', 'descricao', 'tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

    def form_valid(self, form):
        user = self.request.user
        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, permita que ele crie o conteúdo
            form.instance.usuario = user
            return super().form_valid(form)
        else:
            # Se o usuário não pertencer a nenhum desses grupos, verifique se a grade pertence ao mesmo setor
            grade = form.instance.conteudo.first().grade_set.first()
            if grade and grade.setor.membros.filter(id=user.id).exists():
                return super().form_valid(form)
            else:
                # Se não pertencer ao mesmo setor, não permita criar o conteúdo
                return self.handle_no_permission()
            
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Conteúdo"
        context['botao'] = "Cadastrar"
        return context
    

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