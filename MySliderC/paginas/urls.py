from django.urls import path
from .views import IndexView, MenuView



urlpatterns = [
    # path('/endereço/'), MinhaView.as_view(), name='nome-da-url'),
    path('inicio/', IndexView.as_view(), name='inicio'),
    path('menu/', MenuView.as_view(), name='menu'),
   
   
]
