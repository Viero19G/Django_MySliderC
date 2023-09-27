from typing import Any
from django.views.generic.edit import UpdateView
from carrosselApp.models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from usuarios.models import *

class PerfilUpdate(UpdateView):
    template_name = 'cadastros/create.html'
    model = Perfil
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
    
    def get_context_data(self,*args, **kwargs):
       context = super().get_context_data(*args,**kwargs)

       context['titulo'] = 'Meus Dados Pessoais'
       context['botao'] = 'Atualizar'
       return context