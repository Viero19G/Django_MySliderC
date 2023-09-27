from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from usuarios.forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from usuarios.models import Perfil

class UsuarioCreate(CreateView):
    template_name = "cadastros/create.html"
    form_class = UsuarioForm
    success_url= reverse_lazy('login')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='usuario') # busca grupo

        url = super().form_valid(form)  # Cria o objeto

        self.object.groups.add(grupo) # pega objeto e define grupo
        self.object.save() # salva objeto com novo grupo antes de retornar

        Perfil.objects.create(usuario=self.object) ## Cria perfil associado ao user criado

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registrar Novo Usuário"
        context['botao'] = "Cadastrar"
        return context