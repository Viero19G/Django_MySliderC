# forms.py

from django import forms
from carrosselApp.models import Imagem, Video

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['title', 'sub_title', 'descricao', 'tempo', 'image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'sub_title', 'descricao', 'duracao', 'video']
