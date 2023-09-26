from django.db import models
from distutils.command.upload import upload
from django.forms import CheckboxSelectMultiple 
from django.contrib.auth.models import User
from django.contrib.auth import get_user
# Classes e modelos para a construção de todo o projeto
# associados ao bando de dados com os comandos _py manage.py makemigrations
# e py manage.py migrate _ após esses comandos os models são incorporados ao
# sqlite.
class Conteudo(models.Model):
    image = models.ImageField(upload_to='pics/%Y/%m/%d/')
    title = models.CharField(max_length=150, verbose_name='Título')
    sub_title = models.CharField(max_length=200, verbose_name='Sub-Título')
    descricao = models.CharField(max_length=200, verbose_name='Descrição')
    tempo = models.PositiveBigIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)

    def save(self, *args, **kwargs):
        if not self.usuario_id:
            self.usuario = get_user()
        super(Conteudo, self).save(*args, **kwargs)

    def __str__(self):
        return "{} ({})".format(self.title, self.sub_title)

class Grade(models.Model):
    conteudo = models.ManyToManyField(Conteudo, blank=True, verbose_name='Conteúdo')
    title = models.CharField(max_length=150, verbose_name='Título')
    sub_title = models.CharField(max_length=200, verbose_name='Sub-Título')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', default=None)
    usuariosEdit = models.ManyToManyField(User, related_name='grades_editadas', blank=True, verbose_name='Editores de Grade')

    def __str__(self):
        return "{} ({})".format(self.title, ', '.join([str(c) for c in self.conteudo.all()]))

class Setor(models.Model): 
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, verbose_name='Grade', default=None)
    nome = models.CharField(max_length=180, verbose_name='Nome')
    membros = models.ManyToManyField(User, related_name='setores_membros', blank=True, verbose_name='Membros do Setor')

    def __str__(self):
        return "{} ({})".format(self.nome, self.grade.title)