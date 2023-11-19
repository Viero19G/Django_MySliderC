# forms.py

from django import forms
from carrosselApp.models import Imagem, Video, Planilha, Grade


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
        fields = ['planilha_url', 'title', 'sub_title', 'descricao', 'tempo']


class PlanilhaUpForm(forms.ModelForm):
    class Meta:
        model = Planilha
        fields = ['planilha_id', 'title', 'sub_title', 'descricao', 'tempo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tornar o campo planilha_id readonly
        self.fields['planilha_id'].widget.attrs['readonly'] = True


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['title', 'sub_title', 'conteudo', 'setor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione um campo extra para armazenar a URL do conteúdo
        self.fields['conteudo_url'] = forms.CharField(
            widget=forms.HiddenInput(), required=False)
