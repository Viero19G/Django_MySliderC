from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists(): # verifica se é verdadeiro
            raise ValidationError("O email {} informado já está em uso.".format(email)) # se for aparece a mensagem de erro
        return email # sem o return função não funciona
