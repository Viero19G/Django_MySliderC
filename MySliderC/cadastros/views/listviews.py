from django.views.generic.list import ListView   ##### views para listar
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin



class SetorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Setor
    template_name = 'cadastros/listas/setor.html'
    paginate_by = 10

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
    paginate_by = 10

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
   
    @login_required(login_url='login')  # Usar o decorator login_required para exigir autenticação
    def ver_grade(request, grade_id):
        grade = get_object_or_404(Grade, pk=grade_id)

        # Verificar se o usuário é um editor de grade ou pertence a um setor onde a grade aparecerá
        if request.user in grade.usuariosEdit.all() or request.user.setor_set.filter(grades_editadas=grade).exists():
            return render(request, 'ver/verGrade.html', {'grade': grade})
        else:
            # O usuário não tem permissão para visualizar esta grade
           
            return render(request, 'falha') 

    @login_required(login_url='login')  # Usar o decorator login_required para exigir autenticação
    def ver_carrossel(request, grade_id):
        grade = get_object_or_404(Grade, pk=grade_id)

        # Verificar se o usuário é um editor de grade ou pertence a um setor onde a grade aparecerá
        if request.user in grade.usuariosEdit.all() or request.user.setor_set.filter(grades_editadas=grade).exists():
            return render(request, 'ver/verCarrossel.html', {'grade': grade})
        else:
            # O usuário não tem permissão para visualizar este carrossel
           
            return render(request, 'falha') 
        

class ConteudoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Conteudo
    template_name = 'cadastros/listas/conteudo.html'
    paginate_by = 10

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

class VideoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Video
    template_name = 'cadastros/listas/video.html'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user

        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, mostre todo o conteúdo
            queryset = Video.objects.all()
        else:
            # Se não pertencer a nenhum desses grupos, liste apenas o conteúdo do próprio usuário
            queryset = Video.objects.filter(usuario=user)

        return queryset
    
class ImagemList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Imagem
    template_name = 'cadastros/listas/imagem.html'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user

        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, mostre todo o conteúdo
            queryset = Imagem.objects.all()
        else:
            # Se não pertencer a nenhum desses grupos, liste apenas o conteúdo do próprio usuário
            queryset = Imagem.objects.filter(usuario=user)

        return queryset
    
