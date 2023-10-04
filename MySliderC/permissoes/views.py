from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator  # Importe isso

from permissoes.forms.forms import GrupoForm

def user_is_admin(user):
    return user.groups.filter(name='administrador').exists()

@method_decorator(user_passes_test(user_is_admin), name='get')
@method_decorator(user_passes_test(user_is_admin), name='post')
class ManageGroupsView(LoginRequiredMixin, View):
    # Substitua pela URL de login apropriada
    # Substitua pelo campo de redirecionamento apropriado se necessário
   

    def get(self, request):
        groups = Group.objects.all()
        form = GrupoForm()
        return render(request, 'permissoes/controle_grupos.html', {'groups': groups, 'form': form})

    def post(self, request):
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_groups')

        groups = Group.objects.all()
        return render(request, 'permissoes/controle_grupos.html', {'groups': groups, 'form': form})
