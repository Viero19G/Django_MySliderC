from django.contrib.auth.models import User, Group
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

class UserListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = 'cadastros/listas/usuario.html'  # Substitua pelo seu nome de template
    context_object_name = 'users'  # Nome do objeto de contexto na template
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user

        # Verifique se o usuário pertence ao grupo 'administrador'
        admin_group = Group.objects.get(name='administrador')

        if user.groups.filter(name='administrador').exists():
            # Se o usuário for administrador, mostre todos os usuários
            queryset = User.objects.all()
        else:
            # Se o usuário não for administrador, mostre apenas o próprio usuário
            queryset = User.objects.filter(pk=user.pk)

        return queryset
