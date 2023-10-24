from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    tipo_usuario = forms.ChoiceField(
        choices=(('administrador', 'Administrador'),
                 ('operador_marketing', 'Operador de Marketing'),
                 ('usuario', 'Usuário')),
        widget=forms.RadioSelect,
        required=True,
        initial='usuario'  # Defina o valor inicial padrão
    )
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Inclua 'password1' e 'password2' aqui

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "O email {} informado já está em uso.".format(email))
        return email
