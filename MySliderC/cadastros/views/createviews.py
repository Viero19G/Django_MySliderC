from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from moviepy.editor import VideoFileClip
import os
from carrosselApp.models import *
from django.contrib.auth.models import Group
from django.db.models import Q
from datetime import datetime


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
    fields = ['video', 'title', 'sub_title', 'descricao', 'tempo']
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
