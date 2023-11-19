from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/user_list.html'
    context_object_name = 'users'
    login_url = reverse_lazy('inicio')

    def get(self, request):
        # Verificar se o usuário é superuser
        if not request.user.is_superuser:
            return redirect('inicio')

        # Recuperar a lista de usuários
        users = User.objects.all()

        context = {'users': users}
        return render(request, self.template_name, context)
