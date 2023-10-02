from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from usuarios.forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from usuarios.models import Perfil


class UsuarioCreate(CreateView):
    template_name = "cadastros/createUser.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

     # Determine o tipo de usuário com base no campo enviado na requisição
        tipo_usuario = self.request.POST.get('tipo_usuario')

    # Determine o grupo com base no tipo de usuário
        grupo = None

        if tipo_usuario == 'administrador':
            grupo = get_object_or_404(Group, name='administrador')
        elif tipo_usuario == 'operador_marketing':
            grupo = get_object_or_404(Group, name='operador_marketing')
        elif tipo_usuario == 'usuario':
            grupo = get_object_or_404(Group, name='usuario')

        if grupo:
            # Crie o objeto de usuário
            url = super().form_valid(form)

        # Atribua o usuário ao grupo desejado
            self.object.groups.add(grupo)
            self.object.save()

        # Crie um perfil associado ao usuário
            Perfil.objects.create(usuario=self.object)

            return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registrar Novo Usuário"
        context['botao'] = "Cadastrar"
        return context
