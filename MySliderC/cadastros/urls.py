from django.urls import path
# importando views para create
from cadastros.views.createviews import *
# importando views de update
from cadastros.views.upviews import *
# importando views de delete
from cadastros.views.deleteviews import *
# Importando view para listar
from cadastros.views.listviews import * 



urlpatterns = [
    # Para verGrade
    path('ver_grade/<int:grade_id>/', GradeList.ver_grade, name='verGrade'),

    #  Para verCarrossel
    path('ver_Carrossel/<int:grade_id>/',
         GradeList.ver_carrossel, name='verCarrossel'),

    # operações para Grade
    path('editar/grade/<int:pk>/', GradeUpdate.as_view(), name='upGrade'),
    path('listar/grade/', GradeList.as_view(), name='listGrade'),
    path('excluir/grade/<int:pk>/', GradeDelete.as_view(), name='delGrade'),
    path('grade/', GradeCreate.as_view(), name='cadastrar-grade'),

    # operações para Setor
    path('listar/setor/', SetorList.as_view(), name='listSetor'),
    path('editar/setor/<int:pk>/', SetorUpdate.as_view(), name='upSetor'),
    path('excluir/setor/<int:pk>/', SetorDelete.as_view(), name='delSetor'),
    path('setor/', SetorCreate.as_view(), name='cadastrar-setor'),

    # operações para Conteudo
    path('excluir/conteudo/<int:pk>/',
         ConteudoDelete.as_view(), name='delConteudo'),
    path('conteudo/', ConteudoCreate.as_view(), name='cadastrar-conteudo'),
    path('listar/conteudo/', ConteudoList.as_view(), name='listConteudo'),
    path('editar/conteudo/<int:pk>/', ConteudoUpdate.as_view(), name='upConteudo'),

    # operações para Video
    path('excluir/video/<int:pk>/', VideoDelete.as_view(), name='delVideo'),
    path('video/', VideoCreate.as_view(), name='cadastrar-video'),
    path('listar/video/', VideoList.as_view(), name='listVideo'),
    path('editar/video/<int:pk>/', VideoUpdate.as_view(), name='upVideo'),

    # operações para Imagem
    path('excluir/imagem/<int:pk>/', ImagemDelete.as_view(), name='delImagem'),
    path('imagem/', ImagemCreate.as_view(), name='cadastrar-imagem'),
    path('listar/imagem/', ImagemList.as_view(), name='listImagem'),
    path('editar/imagem/<int:pk>/', ImagemUpdate.as_view(), name='upImagem'),

   # operações para planilha
    path('criar_planilha/', PlanilhaCreateView.as_view(), name='cadastrar-planilha'),

]
