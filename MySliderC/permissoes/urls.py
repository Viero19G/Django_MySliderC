# urls.py
from django.urls import path
from permissoes.views import ManageGroupsView

urlpatterns = [
    path('controleGrupos/', ManageGroupsView.as_view(), name='controleGrupos'),
]