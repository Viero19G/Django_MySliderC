from django.db import models
from distutils.command.upload import upload
from django.forms import CheckboxSelectMultiple 
# Classes e modelos para a construção de todo o projeto
# associados ao bando de dados com os comandos _py manage.py makemigrations
# e py manage.py migrate _ após esses comandos os models são incorporados ao
# sqlite.


class Conteudo(models.Model):
    image = models.ImageField(upload_to='pics/%y/%m/%d/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    tempo = models.PositiveBigIntegerField()

    def __str__(self):
        return "{} ({}) ".format(self.title, self.sub_title)

class Grade(models.Model):
    conteudo = models.ManyToManyField(Conteudo, blank=True)  # Use ManyToManyField para permitir múltiplas seleções
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200)

    def __str__(self):
        return "{} ({})".format(self.title, ', '.join([str(c) for c in self.conteudo.all()]))

class Setor(models.Model): 
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, default=None)
    nome=models.CharField(max_length=180)
    def __str__(self):
        return "{} ({}) ".format(self.nome, self.grade.title)

class Usuario(models.Model):
    usrNome=models.CharField(max_length=100)
    usrSenha=models.CharField(max_length=100)
    usrMail=models.EmailField(unique=True)  # 'unique=True' garante que cada e-mail seja único no banco de dados
    # Outros campos do usuário
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    def __str__(self):
        return "{} ({}) ".format(self.usrNome, self.setor.nome)
    
class Perfil(models.Model):
    perfilNome=models.CharField(max_length=100)
    descricao=models.CharField(max_length=300)

    def __str__(self):
        return "{} ({}) ".format(self.perfilNome, self.descricao)
    

class Perfil_Usuario(models.Model):
    descricao=models.CharField(max_length=300)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    def __str__(self):
        return "{} ({}) ({})".format(self.descricao, self.usuario.usrNome, self.perfil.perfilNome)
