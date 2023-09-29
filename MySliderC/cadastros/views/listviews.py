from django.views.generic.list import ListView   ##### views para listar
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin


class SetorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Setor
    template_name = 'cadastros/listas/setor.html'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user

        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, mostre todos os setores
            queryset = Setor.objects.all()
        else:
            # Se não pertencer a nenhum desses grupos, liste apenas o setor do usuário
            queryset = Setor.objects.filter(membros=user)

        return queryset

class GradeList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Grade
    template_name = 'cadastros/listas/grade.html'

    def get_queryset(self):
        user = self.request.user

        # Verifique se o usuário pertence aos grupos 'admin' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, mostre todas as grades
            queryset = Grade.objects.all()
        else:
            try:
                # Tente encontrar o setor do usuário
                setor_do_usuario = Setor.objects.filter(membros=user).first()

                if setor_do_usuario:
                    # Se o usuário pertencer a um setor, liste as grades apenas desse setor
                    queryset = Grade.objects.filter(setor=setor_do_usuario)
                else:
                    # Se o usuário não pertencer a nenhum setor, retorne um conjunto vazio
                    queryset = Grade.objects.none()
            except Setor.DoesNotExist:
                queryset = Grade.objects.none()

        return queryset
    
    def ver_grade(request, grade_id):
        grade = get_object_or_404(Grade, pk=grade_id)
        return render(request, 'ver/verGrade.html', {'grade': grade})
    def ver_carrossel(request, grade_id):
        grade = get_object_or_404(Grade, pk=grade_id)
        return render(request, 'ver/verCarrossel.html', {'grade': grade})


class ConteudoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Conteudo
    template_name = 'cadastros/listas/conteudo.html'
    

    def get_queryset(self):
        user = self.request.user

        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, mostre todo o conteúdo
            queryset = Conteudo.objects.all()
        else:
            # Se não pertencer a nenhum desses grupos, liste apenas o conteúdo do próprio usuário
            queryset = Conteudo.objects.filter(usuario=user)

        return queryset


# class UsuarioList(LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     model = Usuario
#     template_name = 'cadastros/listas/usuario.html'

# class PerfilList(LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     model = Perfil
#     template_name = 'cadastros/listas/perfil.html'

# class Perfil_UsuarioList(LoginRequiredMixin, ListView):
#     login_url = reverse_lazy('login')
#     model = Perfil_Usuario
#     template_name = 'cadastros/listas/perfilUsuario.html'