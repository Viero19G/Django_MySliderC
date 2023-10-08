from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user

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
        raise ValidationError('Somente imagens JPG, JPEG, PNG e GIF são permitidas.')

class Setor(models.Model): 
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)
    nome = models.CharField(max_length=180, verbose_name='Nome do SETOR')
    membros = models.ManyToManyField(User, related_name='setores_membros', blank=True, verbose_name='Selecione os Membros do Setor')

    def __str__(self):
        return "{} ".format(self.nome)

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
    )

    tipo = models.CharField(max_length=10, null=True, blank=True, choices=TIPO_CHOICES)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    imagem = models.ForeignKey(Imagem, on_delete=models.CASCADE, null=True, blank=True)
   

class Grade(models.Model):
    setor = models.ManyToManyField(Setor, related_name='grades_editadas', blank=True, verbose_name='Setores Onde Aparecerá')
    conteudo = models.ManyToManyField(Conteudo, blank=True, verbose_name='Conteúdo')
    title = models.CharField(max_length=150, verbose_name='Título')
    sub_title = models.CharField(max_length=200, verbose_name='Sub-Título')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)
    usuariosEdit = models.ManyToManyField(User, related_name='grades_editadas', blank=True, verbose_name='Editores de Grade')

    def __str__(self):
        return "{} ({})".format(self.title, ', '.join([str(c) for c in self.conteudo.all()]))