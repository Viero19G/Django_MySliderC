from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from integracao.google_sheets_utils import authenticate_google_sheets
from googleapiclient.discovery import build
import requests
import re
from django.utils import timezone
import os

# Classes e modelos para a construção de todo o projeto
# associados ao banco de dados com os comandos _py manage.py makemigrations
# e py manage.py migrate _ após esses comandos os models são incorporados ao
# SQLite.


def validate_video_extension(value):
    allowed_extensions = ['mp4', 'avi', 'mkv', 'mov']
    extension = value.name.split('.')[-1].lower()
    if extension not in allowed_extensions:
        raise ValidationError(
            'Somente vídeos MP4, AVI, MKV e MOV são permitidos.')


def validate_image_extension(value):
    allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
    extension = value.name.split('.')[-1].lower()
    if extension not in allowed_extensions:
        raise ValidationError(
            'Somente imagens JPG, JPEG, PNG e GIF são permitidas.')


class Setor(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)
    nome = models.CharField(max_length=180, verbose_name='Nome do SETOR')
    membros = models.ManyToManyField(
        User, related_name='setores_membros', blank=True, verbose_name='Selecione os Membros do Setor')

    def __str__(self):
        return "{} ".format(self.nome)


class Planilha(models.Model):
    planilha_id = models.CharField(
        max_length=255, verbose_name='ID da Planilha Google')
    title = models.CharField(max_length=150, verbose_name='Título')
    sub_title = models.CharField(max_length=200, verbose_name='Sub-Título')
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)
    tempo = models.PositiveBigIntegerField(blank=True, null=True)

    def extrair_id_da_planilha(url):
        # Padrão de expressão regular para encontrar o ID da planilha
        padrao = r"/d/([a-zA-Z0-9-_]+)"

        # Tente encontrar uma correspondência com o padrão na URL
        correspondencia = re.search(padrao, url)

        if correspondencia:
            # Se houver uma correspondência, retorne o grupo capturado (ID da planilha)
            return correspondencia.group(1)

        # Se não houver correspondência, retorne None para indicar que o ID não pôde ser encontrado
        return None

    def obter_links_de_download(token, planilha_id):
        # Autenticação e obtenção do token de acesso (você precisa implementar essa função)
        gc, access_token = authenticate_google_sheets()
        

        # Cabeçalhos da solicitação
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {access_token}"
        }

        # Parâmetros a serem enviados na solicitação
        params = {
            "planilhaId": planilha_id,  # Substitua pela ID da sua planilha
            "token": access_token
        }

        # URL do script do Google Apps
        apps_script_url = "https://script.google.com/macros/s/AKfycbwzb4iWFAoFwnD6iKlHLb_t5dk-tu9CI7PwgkrMwUoMG8G6AYAunfaogxt_wxL3qRnQoQ/exec"

        # Faça a solicitação GET para a URL original
        response = requests.get(apps_script_url, params=params, headers=headers)

        # Verifique se a resposta contém um URL de redirecionamento
        if response.status_code == 302:
            # URL de redirecionamento
            redirect_url = response.headers['Location']

            # Faça uma nova solicitação GET para o URL de redirecionamento
            response = requests.get(redirect_url, headers=headers)

            # Verifica se a solicitação foi bem-sucedida (código 200)
            if response.status_code == 200:
                # O conteúdo da resposta é um JSON que você pode processar
                data = response.json()
                print(data)
            else:
                # Em caso de erro, imprima o código de status e o conteúdo da resposta
                print(f"Erro {response.status_code}: {response.text}")

        else:
            # Se não houver redirecionamento, a resposta contém o JSON desejado
            try:
                data = response.json()
                print(data)
            except ValueError as e:
                # A resposta não é um JSON válido
                print(f"Erro ao analisar JSON: {e}")
                print(f"Resposta: {response.text}")

    # define para onde sera o UpLoad dos arquivos
    def upload_to_path(instance, filename):
        # Gera o caminho de upload dinâmico
        return os.path.join(
            'graficos',
            timezone.now().strftime('%Y/%m/%d'),
            filename
        )

    # Usadda para alterar as configurações de compartilhamento das imagens criadas pelo apps scripts
    def alterar_configuracoes_compartilhamento(imagem_url):
        # Obtenha as credenciais e crie uma instância do serviço Google Drive
        creds, token = authenticate_google_sheets()
        print(f"token de acesso:  {creds}")
        breakpoint()
        drive_service = build('drive', 'v2', credentials=creds)
        # Extraia o ID do arquivo da imagem URL
        file_id = imagem_url.split('=')[1]

        # Defina as configurações de compartilhamento desejadas
        permissions = {
            'role': 'writer',  # Permite edição
            'type': 'anyone',
        }

        # Atualize as permissões do arquivo
        drive_service.permissions().create(
            fileId=file_id,
            body=permissions,
        ).execute()

        print(f"Configurações de compartilhamento alteradas para {imagem_url}")
        breakpoint()


class Grafico(models.Model):
    image = models.FileField(
        upload_to=Planilha.upload_to_path,
        verbose_name='Imagem',
        validators=[validate_image_extension])
    descricao = models.CharField(max_length=200, verbose_name='Descrição')


class GraficoPlanilha(models.Model):
    planilha = models.ForeignKey(Planilha, on_delete=models.PROTECT)
    grafico = models.ForeignKey(Grafico, on_delete=models.CASCADE)


class Video(models.Model):
    video = models.FileField(
        upload_to='videos/%Y/%m/%d/',
        verbose_name='Vídeo',
        validators=[validate_video_extension]
    )
    title = models.CharField(max_length=150, verbose_name='Título')
    sub_title = models.CharField(max_length=200, verbose_name='Sub-Título')
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    tempo = models.PositiveBigIntegerField(blank=True, null=True)
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)

    def save(self, *args, **kwargs):
        if not self.usuario_id:
            self.usuario = get_user()
        super(Video, self).save(*args, **kwargs)

    def clean(self):
        if self.video:
            validate_video_extension(self.video)

    def __str__(self):
        return "{} ({})".format(self.title, self.sub_title)


class Imagem(models.Model):
    image = models.FileField(
        upload_to='pics/%Y/%m/%d/',
        verbose_name='Imagem',
        validators=[validate_image_extension]
    )
    title = models.CharField(max_length=150, verbose_name='Título')
    sub_title = models.CharField(max_length=200, verbose_name='Sub-Título')
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    tempo = models.PositiveBigIntegerField(blank=True, null=True)
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)

    def save(self, *args, **kwargs):
        if not self.usuario_id:
            self.usuario = get_user()
        super(Imagem, self).save(*args, **kwargs)

    def clean(self):
        if self.image:
            validate_image_extension(self.image)

    def __str__(self):
        return "{} ({})".format(self.title, self.sub_title)


class Conteudo(models.Model):
    TIPO_CHOICES = (
        ('video', 'Vídeo'),
        ('imagem', 'Imagem'),
        ('planilha', 'Planilha'),
    )

    tipo = models.CharField(max_length=10, null=True,
                            blank=True, choices=TIPO_CHOICES)
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, null=True, blank=True)
    imagem = models.ForeignKey(
        Imagem, on_delete=models.CASCADE, null=True, blank=True)
    planilha = models.ForeignKey(
        Planilha, on_delete=models.CASCADE, null=True, blank=True)


class Grade(models.Model):
    setor = models.ManyToManyField(
        Setor, related_name='grades_editadas', blank=True, verbose_name='Setores Onde Aparecerá')
    conteudo = models.ManyToManyField(
        Conteudo, blank=True, verbose_name='Conteúdo')
    title = models.CharField(max_length=150, verbose_name='Título')
    sub_title = models.CharField(max_length=200, verbose_name='Sub-Título')
    usuario = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)
    usuariosEdit = models.ManyToManyField(
        User, related_name='grades_editadas', blank=True, verbose_name='Editores de Grade')

    def __str__(self):
        return "{} ({})".format(self.title, ', '.join([str(c) for c in self.conteudo.all()]))
