from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from moviepy.editor import VideoFileClip
import os
from cadastros.formsPersonalizados.forms import PlanilhaForm
from carrosselApp.models import *
from django.contrib.auth.models import Group, User
from django.db.models import Q
from django.contrib import messages
from integracao.google_sheets_utils import authenticate_google_sheets
from django.core.files.base import ContentFile
import gdown
from django.utils import timezone


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
    fields = ['tipo', 'video', 'imagem',]
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


class VideoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Video
    fields = ['video', 'title', 'sub_title', 'descricao']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listVideo')

    def form_valid(self, form):
        user = self.request.user

        # Verifique se o usuário pertence aos grupos 'administrador' ou 'marketing'
        admin_group = Group.objects.get(name='administrador')
        marketing_group = Group.objects.get(name='marketing')

        if user.groups.filter(Q(name='administrador') | Q(name='marketing')).exists():
            # Se o usuário pertencer a qualquer um dos grupos, permita que ele crie o conteúdo
            form.instance.usuario = user
            # atenção url default do django usa barras normais e para encontrar o arquivo no windows
            # é necessário usar barras invertidas
            enviar = super().form_valid(form)
            caminho = r'C:\Users\gabri\Documents\projetos_django\DjangoProjeto_II\MySliderC'

            # Obtenha o caminho correto do vídeo usando o método url do campo FileField
            video_path = form.instance.video.url
            print(f"Caminho do vídeo: {video_path}")

            # Adicione '/pics/videos/' à parte inicial do caminho do vídeo

            # Certifique-se de que o caminho comece com '/media/' para que seja um caminho absoluto completo
            if video_path.startswith('/media/'):
                # Remova '/media/' para obter o caminho relativo real
                video_path = video_path[len('/media/'):]

            formata_win = os.path.normpath(video_path)
            buscar_em = caminho + formata_win
            try:
                with VideoFileClip(buscar_em) as clip:
                    form.instance.tempo = int(clip.duration)
            except Exception as e:
                print(f"Erro ao obter a duração do vídeo: {e}")

            # Salvar o formulário novamente para adicionar o tempo
            enviar = super().form_valid(form)

            # Obter o objeto de vídeo após salvar novamente o formulário
            # Obter o objeto de vídeo diretamente do formulário
            video_obj = form.instance

            # Definir o tempo do objeto de vídeo com base no formulário
            video_obj.tempo = form.instance.tempo
            video_obj.save()

            return enviar

        else:
            # Se o usuário não pertencer a nenhum desses grupos, verifique se a grade pertence ao mesmo setor
            grade = form.instance.conteudo.first().grade_set.first()
            if grade and grade.setor.membros.filter(id=user.id).exists():

                enviar = super().form_valid(form)
                caminho = r'C:\Users\gabri\Documents\projetos_django\DjangoProjeto_II\MySliderC'

                # Obtenha o caminho correto do vídeo usando o método url do campo FileField
                video_path = form.instance.video.url
                print(f"Caminho do vídeo: {video_path}")

                # Adicione '/pics/videos/' à parte inicial do caminho do vídeo

                # Certifique-se de que o caminho comece com '/media/' para que seja um caminho absoluto completo
                if video_path.startswith('/media/'):
                    # Remova '/media/' para obter o caminho relativo real
                    video_path = video_path[len('/media/'):]

                formata_win = os.path.normpath(video_path)
                buscar_em = caminho + formata_win
                try:
                    with VideoFileClip(buscar_em) as clip:
                        form.instance.tempo = int(clip.duration)
                except Exception as e:
                    print(f"Erro ao obter a duração do vídeo: {e}")

                # Salvar o formulário novamente para adicionar o tempo
                enviar = super().form_valid(form)

                # Obter o objeto de vídeo diretamente do formulário
                video_obj = form.instance

                # Definir o tempo do objeto de vídeo com base no formulário
                video_obj.tempo = form.instance.tempo
                video_obj.save()

                return enviar
            else:
                # Se não pertencer ao mesmo setor, não permita criar o conteúdo
                return self.handle_no_permission()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Video"
        context['botao'] = "Cadastrar"
        return context


class ImagemCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Imagem
    fields = ['image', 'title', 'sub_title', 'descricao', 'tempo']
    template_name = 'cadastros/create.html'
    success_url = reverse_lazy('listImagem')

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

        context['titulo'] = "Cadastro de Imagem"
        context['botao'] = "Cadastrar"
        return context


class PlanilhaCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Planilha
    form_class = PlanilhaForm
    template_name = 'cadastros/createPlanilha.html'
    success_url = reverse_lazy('listPlanilha')

    def form_valid(self, form):
        # Extrair o link da planilha a partir do formulário
        planilha_url = Planilha.extrair_id_da_planilha(
            form.cleaned_data['planilha_url'])

        if planilha_url:
            # Atribuir o usuário atual ao campo usuario
            form.instance.usuario = self.request.user

            # Armazenar o link da planilha no banco de dados
            form.instance.planilha_id = planilha_url
            Planilha_Id = form.instance.planilha_id

            # Autenticar e obter token
            gc, access_token = authenticate_google_sheets()

            # Salvar a Planilha fora do loop de imagens
            verifica_graficos = Planilha.obter_links_de_download(
                access_token, Planilha_Id)
            print("Verificação de gráficos:", verifica_graficos)
            breakpoint()

            # Se "imagens" estiver presente e não vazio, processar as imagens
            if "imagens" in verifica_graficos and verifica_graficos["imagens"]:
                self.processar_imagens(verifica_graficos["imagens"], gc)

            else:
                messages.warning(
                    self.request, "Nenhum gráfico presente nessa planilha.")
                # Não há imagens, mas salva a planilha
                return super().form_valid(form)

            return super().form_valid(form)
        else:
            messages.error(self.request, "Erro ao extrair link da planilha.")
            return self.form_invalid(form)

    def processar_imagens(self, imagens, gc):
        for imagem_url in imagens:
            filename = self.obter_nome_do_arquivo(imagem_url)
            output_path = Planilha.upload_to_path(self, filename)
            print("Salvando em:", output_path)
            breakpoint()

            # Certifique-se de que o diretório existe
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            # Fazer o download da imagem usando gdown
            imagem_url_com_token = f"{imagem_url}&access_token={gc.auth.access_token}"
            Planilha.alterar_configuracoes_compartilhamento(imagem_url)
            gdown.download(imagem_url_com_token, output_path, quiet=False)
            print("Download concluído")
            breakpoint()

            # Criar um objeto Grafico
            grafico = Grafico()
            grafico.descricao = "Automatizado"

            # Salvar a imagem no objeto Grafico
            with open(output_path, 'rb') as f:
                grafico.image.save(filename, ContentFile(f.read()), save=True)

            # Criar a relação GraficoPlanilha
            grafico_planilha = GraficoPlanilha(planilha=self, grafico=grafico)
            grafico_planilha.save()

    def obter_nome_do_arquivo(self, imagem_url):
        # Usar split para obter o nome do arquivo da URL
        filename = imagem_url.split("/")[-1].split("?")[0]
        # Certificar-se de que o nome do arquivo não contém caracteres inválidos
        return re.sub(r"[^a-zA-Z0-9_.-]", "_", filename)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Compartilhando Planilha"
        context['botao'] = "Compartilhar"
        return context
