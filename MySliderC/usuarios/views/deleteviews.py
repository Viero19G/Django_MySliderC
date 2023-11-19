from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.shortcuts import redirect

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuarios/user_confirm_delete.html'
    success_url = reverse_lazy('verUsers')

    def get(self, request, *args, **kwargs):
        # Verificar se o usuário é superuser
        if not request.user.is_superuser:
            return redirect('inicio')

        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        # Verificar se o usuário é superuser
        if not request.user.is_superuser:
            return redirect('inicio')

        return super().delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])
