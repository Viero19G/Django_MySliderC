from django.views.generic.edit import DeleteView  # views para Delete
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.contrib import messages

from cadastros.forms.deletePlanilhaForm import PlanilhaDeleteForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import ProtectedError

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


class VideoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Video
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listVideo')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluindo Conteúdo"

        return context


class ImagemDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"administrador"
    model = Imagem
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('listImagem')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluindo Conteúdo"

        return context


class PlanilhaDelete(DeleteView):
    model = Planilha
    template_name = 'cadastros/delete_planilha.html'
    success_url = reverse_lazy('listPlanilha')

    def get(self, request, *args, **kwargs):
        planilha = self.get_object()
        graficos_relacionados = GraficoPlanilha.objects.filter(
            planilha=planilha)
        form = PlanilhaDeleteForm()
        return render(request, self.template_name, {'planilha': planilha, 'graficos_relacionados': graficos_relacionados, 'form': form})

    def post(self, request, *args, **kwargs):
        # Adicione este print para verificar se o método é acessado
        print("Entrou no método post")
        planilha = self.get_object()
        form = PlanilhaDeleteForm(request.POST)
        print(planilha)
        # Moveu a linha para verificar a validade primeiro
        print(form.is_valid())
        if form.is_valid():
            try:
                with transaction.atomic():
                    graficos_relacionados = GraficoPlanilha.objects.filter(
                        planilha=planilha)
                    for relacao in graficos_relacionados:
                        grafico = relacao.grafico
                        print(f"Antes da exclusão do gráfico {grafico.id}")
                        relacao.delete()
                        print(f"Depois da exclusão do gráfico {grafico.id}")

                        # Agora, exclua o gráfico associado
                        print(
                            f"Antes da exclusão do gráfico associado {grafico.id}")
                        grafico.delete()
                        print(
                            f"Depois da exclusão do gráfico associado {grafico.id}")

                    # Adicione este print para verificar se chega até aqui
                    print("Antes da exclusão da planilha")
                    planilha.delete()
                    print("Depois da exclusão da planilha")

                    messages.success(request, "Planilha excluída com sucesso.")
                    return redirect('listPlanilha')

            except ProtectedError as e:
                messages.error(
                    request, f"Erro ao excluir a planilha: {str(e)}")
                return redirect('listPlanilha')
            except Exception as e:
                print(f"Erro não tratado: {str(e)}")
                messages.error(request, "Erro ao excluir a planilha.")
                return redirect('listPlanilha')
        else:
            messages.warning(request, "A exclusão não foi confirmada.")
            return redirect('listPlanilha')

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
