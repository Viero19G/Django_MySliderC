import gspread
import base64
from braces.views import GroupRequiredMixin
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.models import User, Group
from carrosselApp.models import Planilha
from carrosselApp.models import *
from integracao.google_sheets_utils import authenticate_google_sheets


class SetorList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = ["administrador", "marketing"]
    model = Setor
    template_name = 'cadastros/listas/setor.html'

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
                    queryset = Grade.objects.filter(usuariosEdit=user)
                else:
                    queryset = Grade.objects.filter(usuariosEdit=user)
            except Setor.DoesNotExist:
                queryset = Grade.objects.none()

        return queryset

    # Usar o decorator login_required para exigir autenticação
    @login_required(login_url='login')
    def ver_grade(request, grade_id):
        grade = get_object_or_404(Grade, pk=grade_id)

        # Verificar se o usuário é um editor de grade ou pertence a um setor onde a grade aparecerá
        if request.user in grade.usuariosEdit.all() or request.user.setor_set.filter(grades_editadas=grade).exists():
            return render(request, 'ver/verGrade.html', {'grade': grade})
        else:
            # O usuário não tem permissão para visualizar esta grade

            return render(request, 'falha')

    # Usar o decorator login_required para exigir autenticação
    @login_required(login_url='login')
    def ver_carrossel(request, grade_id):
        grade = get_object_or_404(Grade, pk=grade_id)

        # Verificar se o usuário é um editor de grade ou pertence a um setor onde a grade aparecerá
        if request.user in grade.usuariosEdit.all() or request.user.setor_set.filter(grades_editadas=grade).exists():
            # Obter todos os conteúdos associados à grade
            conteudos = grade.conteudo.all()

            # Adicionar informações da planilha à lista de conteúdos, se for o caso
            for conteudo in conteudos:
                if conteudo.tipo == 'planilha':
                    try:
                        graficos_planilha = conteudo.planilha.graficoplanilha_set.all()
         
                        if not graficos_planilha.exists():
                            # Adicione informações da planilha quando não há gráficos associados
                            gc, token = authenticate_google_sheets()
                            planilha_google = gc.open_by_key(conteudo.planilha.planilha_id)
                            abas = planilha_google.worksheets()
                            abas_info = []

                            for aba in abas:
                                data = aba.get_all_values()
                                data = [[value for value in row] for row in data if any(value.strip() for value in row)]

                                abas_info.append({
                                    'aba': aba,
                                    'data': data
                                })

                            conteudo.abas_info = abas_info

                    except gspread.exceptions.APIError as e:
                        return render(request, 'erro.html', {'mensagem': 'Erro ao acessar a planilha'})

            return render(request, 'ver/verCarrossel.html', {'grade': grade, 'conteudos': conteudos})
        else:
            # O usuário não tem permissão para visualizar este carrossel
            return redirect("inicio")


class ConteudoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    # Lista dos nomes dos grupos permitidos
    group_required = ["administrador", "marketing"]
    model = Conteudo
    template_name = 'cadastros/listas/conteudo.html'

    def get_queryset(self):
        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        if self.request.user.groups.filter(name__in=self.group_required).exists():
            # Se o usuário pertencer a qualquer um dos grupos, mostre todo o conteúdo
            queryset = Conteudo.objects.all()
        else:
            # Se o usuário não pertencer aos grupos permitidos, retorne um queryset vazio
            queryset = Conteudo.objects.none()

        return queryset


class VideoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Video
    template_name = 'cadastros/listas/video.html'

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


class PlanilhaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Planilha
    template_name = 'cadastros/listas/planilha.html'

    def get_queryset(self):
        user = self.request.user

        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, mostre todo o conteúdo
            queryset = Planilha.objects.all()
        else:
            # Se não pertencer a nenhum desses grupos, liste apenas o conteúdo do próprio usuário
            queryset = Planilha.objects.filter(usuario=user)

        return queryset

    @login_required(login_url='login')
    def ver_planilha(request, pk):
        planilha = get_object_or_404(Planilha, pk=pk)

        gc, token = authenticate_google_sheets()

        try:
            planilha_google = gc.open_by_key(planilha.planilha_id)
            abas = planilha_google.worksheets()
        except gspread.exceptions.APIError as e:
            return render(request, 'erro.html', {'mensagem': 'Erro ao acessar a planilha'})

        # Lista para armazenar informações sobre as abas
        abas_info = []

        for aba in abas:
            # Obtém os dados da aba, incluindo apenas as linhas e colunas que contêm valores
            data = aba.get_all_values()

            # Remove as linhas e colunas que contêm apenas valores vazios
            data = [[value for value in row]
                    for row in data if any(value.strip() for value in row)]

            # Adiciona informações da aba à lista abas_info
            abas_info.append({
                'aba': aba,
                'data': data
            })
            print(abas_info)

        return render(request, 'ver/verPlanilha.html', {'planilha': planilha, 'abas_info': abas_info})
