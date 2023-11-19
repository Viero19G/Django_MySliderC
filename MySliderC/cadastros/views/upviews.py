from django.views.generic.edit import UpdateView
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect

from cadastros.formsPersonalizados.forms import PlanilhaUpForm, GradeForm
from django.core.files.base import ContentFile
import gdown


class SetorUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Setor
    group_required = ["administrador"]
    fields = ['nome', 'membros']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listSetor')

    def dispatch(self, request, *args, **kwargs):
        setor = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Setor
        if setor.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("inicio")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Setor"
        context['botao'] = "Salvar"
        return context


class GradeUpdate(UpdateView):
    model = Grade
    form_class = GradeForm
    template_name = 'editar/upGrade.html'
    success_url = reverse_lazy('listGrade')

    def get_queryset(self):
        return Grade.objects.all()

    def dispatch(self, request, *args, **kwargs):
        grade = self.get_object()

        if (grade.usuario == request.user or
                request.user.groups.filter(name__in=['administradores', 'marketing']).exists() or
                request.user in grade.usuariosEdit.all()):
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("inicio")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Grade"
        context['botao'] = "Salvar"

        conteudo_urls = []
        for conteudo in self.object.conteudo.all():
            conteudo_url = None

            if conteudo.tipo == 'imagem':
                conteudo_url = conteudo.imagem.title
            elif conteudo.tipo == 'video':
                conteudo_url = conteudo.video.title
            elif conteudo.tipo == 'planilha':
                # ou qualquer informação que você queira exibir
                conteudo_url = f'Planilha: {conteudo.planilha.title}'

            conteudo_urls.append((conteudo, conteudo_url))

        context['conteudo_urls'] = conteudo_urls

        return context


class ConteudoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Conteudo
    fields = ['title', 'sub_title', 'descricao', 'tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

    def dispatch(self, request, *args, **kwargs):
        conteudo = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Conteúdo
        if conteudo.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("inicio")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Conteúdo"
        context['botao'] = "Salvar"
        return context


class VideoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Video
    fields = ['video', 'title', 'sub_title', 'descricao']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

    def dispatch(self, request, *args, **kwargs):
        conteudo = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Conteúdo
        if conteudo.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("inicio")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Video"
        context['botao'] = "Salvar"
        return context


class ImagemUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Imagem
    fields = ['title', 'sub_title', 'descricao', 'tempo', 'image']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listConteudo')

    def dispatch(self, request, *args, **kwargs):
        conteudo = self.get_object()

        # Verifique se o usuário logado é o mesmo que criou o Conteúdo
        if conteudo.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("inicio")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editando Conteúdo"
        context['botao'] = "Salvar"
        return context


class PlanilhaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Planilha
    form_class = PlanilhaUpForm
    template_name = 'editar/upPlanilha.html'
    success_url = reverse_lazy('listPlanilha')
    success_message = "Planilha atualizada com sucesso."

    def dispatch(self, request, *args, **kwargs):
        # Verifica se o usuário logado pertence aos grupos 'administrador' ou 'marketing'
        if request.user.groups.filter(name__in=['administrador', 'marketing']).exists():
            return super().dispatch(request, *args, **kwargs)

        # Obtém a planilha associada à view
        planilha = self.get_object()

        # Verifica se o usuário logado é o mesmo que criou a planilha
        if planilha.usuario == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("inicio")

    def form_valid(self, form):
        # Obtém o objeto da Planilha antes da atualização
        planilha_antiga = self.get_object()

        # Deleta as relações GraficoPlanilha e os gráficos associados
        self.deletar_relacoes_e_graficos(planilha_antiga)

        # Extrai o link da nova planilha a partir do formulário
        planilha_url_nova = Planilha.extrair_id_da_planilha(
            form.cleaned_data['planilha_id'])

        if planilha_url_nova is None:
            # Se for None, use o valor original
            planilha_url_nova = form.cleaned_data['planilha_id']

        if planilha_url_nova:
            # Continue com o processamento normal
            form.instance.usuario = self.request.user
            form.instance.planilha_id = planilha_url_nova
            response = super().form_valid(form)

            gc, access_token = authenticate_google_sheets()

            # Processa e associa gráficos
            verifica_graficos = Planilha.obter_links_de_downlload(
                access_token, form.instance.planilha_id)

            if "imagens" in verifica_graficos and verifica_graficos["imagens"]:
                self.processar_imagens(
                    verifica_graficos["imagens"], access_token, form.instance.pk)
                messages.success(
                    self.request, "Imagens processadas com sucesso.")
            else:
                messages.warning(
                    self.request, "Nenhum gráfico presente nessa planilha.")
                return response

            return response
        else:
            messages.error(self.request, "Erro ao extrair link da planilha.")
            return self.form_invalid(form)

    def deletar_relacoes_e_graficos(self, planilha):
        graficos_relacionados = GraficoPlanilha.objects.filter(
            planilha=planilha)
        for relacao in graficos_relacionados:
            grafico = relacao.grafico
            # Agora, exclua a relação
            relacao.delete()
            # Agora, exclua o gráfico associado
            grafico.delete()

    def processar_imagens(self, imagens, access_token, pk_da_planilha):
        for imagem_url in imagens:
            try:
                # Obtenha o nome do arquivo da URL
                filename = f"{self.obter_nome_do_arquivo(imagem_url)}.png"
                # Construa o caminho do arquivo no qual salvar o gráfico
                output_dir = os.path.join(
                    'pics', 'graficos', timezone.now().strftime('%Y/%m/%d'))
                output_path = os.path.join(output_dir, filename)

                # Certifique-se de que o diretório exista
                os.makedirs(output_dir, exist_ok=True)

                # Fazer o download da imagem usando gdown diretamente no caminho desejado
                imagem_url_com_token = f"{imagem_url}&access_token={access_token}"
                gdown.download(imagem_url_com_token, output_path, quiet=False)

                # Criar um objeto Grafico
                grafico = Grafico(descricao="Automatizado")

                # Usar o contexto with para abrir e ler o arquivo
                with open(output_path, 'rb') as f:
                    grafico.image.save(
                        filename, ContentFile(f.read()), save=True)

                # Relacionar o gráfico à planilha
                # Obtendo a instância da Planilha usando o pk_da_planilha
                planilha_instance = Planilha.objects.get(pk=pk_da_planilha)

                # Criar a relação GraficoPlanilha
                grafico_planilha = GraficoPlanilha(
                    planilha=planilha_instance, grafico=grafico)
                grafico_planilha.save()

            except Exception as e:
                print(f"Erro ao processar imagem: {str(e)}")

    def obter_nome_do_arquivo(self, imagem_url):
        # Usar split para obter o nome do arquivo da URL
        filename = imagem_url.split("/")[-1].split("?")[0]
        # Certificar-se de que o nome do arquivo não contém caracteres inválidos
        return re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)
