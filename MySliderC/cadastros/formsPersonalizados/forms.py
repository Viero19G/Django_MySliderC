# forms.py

from django import forms
from carrosselApp.models import Imagem, Video, Planilha


class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['title', 'sub_title', 'descricao', 'tempo', 'image']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video', 'title', 'sub_title', 'descricao', 'tempo']

        # Personalize o widget do campo "tempo" para torná-lo somente leitura
        widgets = {
            'tempo': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class PlanilhaForm(forms.ModelForm):
    planilha_url = forms.URLField(
        label='Link da Planilha', 
        help_text='Cole o link da planilha que deseja compartilhar', 
        required=True
    )

    class Meta:
        model = Planilha
        fields = ['planilha_url', 'title', 'sub_title', 'descricao']
