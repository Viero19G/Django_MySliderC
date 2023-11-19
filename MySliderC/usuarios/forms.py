from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


class UsuarioForm(LoginRequiredMixin, UserCreationForm):
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
    
class CustomUserChangeForm(LoginRequiredMixin,UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()

class CustomSetPasswordForm(LoginRequiredMixin,SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ('password',)