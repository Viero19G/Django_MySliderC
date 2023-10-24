from django.urls import path
from .views import IndexView, GradeView



urlpatterns = [
    # path('/endereço/'), MinhaView.as_view(), name='nome-da-url'),
    path('inicio/', IndexView.as_view(), name='inicio'),
    path('grade/', GradeView.as_view(), name='grade'),
   
   
]
