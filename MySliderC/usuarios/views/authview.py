from django.shortcuts import redirect
from django.contrib.auth.models import User
from usuarios.models import Perfil
from social_django.models import UserSocialAuth

def social_auth_google_redirect(request):
    user = request.user

    # Verifique se o usuário já está autenticado com o Google
    if not user.is_authenticated:
        return redirect('login')  # Redirecione para a página de login caso não haja autenticação com o Google

    # Verifique se o usuário já possui uma associação com o Google
    if UserSocialAuth.objects.filter(user=user, provider='google-oauth2').exists():
        return redirect('perfil')  # Redirecione para onde você quiser após a autenticação bem-sucedida

    # Caso contrário, associe a conta com o Google
    google_social_auth = UserSocialAuth.create_social_auth(user, user.username, 'google-oauth2', 'google-oauth2-access-token')
    google_social_auth.save()

    # Você pode adicionar tratamento adicional ou personalizar o redirecionamento

    return redirect('perfil')  # Redirecione para onde você quiser após a autenticação bem-sucedida
