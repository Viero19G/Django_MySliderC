from django.views.generic.edit import UpdateView
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from usuarios.models import *
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from usuarios.forms import CustomUserChangeForm, CustomSetPasswordForm
from django.contrib.auth import get_user_model


class PerfilUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'cadastros/create.html'
    model = Perfil
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = 'Meus Dados Pessoais'
        context['botao'] = 'Atualizar'
        return context


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'usuarios/user_edit.html'
    success_url = reverse_lazy('user_list')

    def get(self, request, *args, **kwargs):
        # Verificar se o usuário é superuser
        if not request.user.is_superuser:
            return redirect('inicio')

        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Verificar se o usuário é superuser
        if not request.user.is_superuser:
            return redirect('inicio')

        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')  # Obtém o ID do usuário da URL
        return get_object_or_404(User, pk=user_id) 

    def get_success_url(self):
        return reverse_lazy('verUsuarios')


class CustomSetPasswordView(LoginRequiredMixin, PasswordChangeView):
    form_class = CustomSetPasswordForm
    template_name = 'usuarios/user_pass.html'
    # Substitua 'user_list' pela URL desejada após a alteração da senha
    success_url = reverse_lazy('verUsuarios')

    def get_user(self):
        user_id = self.kwargs.get('user_id')
        return get_object_or_404(get_user_model(), pk=user_id)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.get_user()
        return kwargs
