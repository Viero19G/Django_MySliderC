from django.db import models
from distutils.command.upload import upload
# Classes e modelos para a construção de todo o projeto
# associados ao bando de dados com os comandos _py manage.py makemigrations
# e py manage.py migrate _ após esses comandos os models são incorporados ao
# sqlite.


class Carousel(models.Model):
    image = models.ImageField(upload_to='pics/%y/%m/%d/')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    tempo = models.PositiveBigIntegerField()

    def __str__(self):
        return "{} ({}) ".format(self.title, self.image)

class Tela(models.Model):
    carrossel = models.ForeignKey(Carousel, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Setor(models.Model):
    tela = models.ForeignKey(Tela, on_delete=models.CASCADE)
    nome=models.CharField(max_length=180)
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    usrNome=models.CharField(max_length=100)
    usrSenha=models.CharField(max_length=100)
    usrMail=models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    def __str__(self):
        return self.usrNome
    
class Perfil(models.Model):
    perfilNome=models.CharField(max_length=100)
    descricao=models.CharField(max_length=300)

    def __str__(self):
        return self.perfilNome
    

class Perfil_Usuario(models.Model):
    descricao=models.CharField(max_length=300)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    def __str__(self):
        return self.descricao
    
