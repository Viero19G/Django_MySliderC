from django.views.generic import TemplateView
from carrosselApp.models import Conteudo


class IndexView(TemplateView):
    template_name = "paginas/index.html"

class GradeView(TemplateView):
    template_name = "paginas/grade.html"

# class grade_conteudo(request):
#     obj = Conteudo.objects.all()
#     context = {
#         'obj':obj
#     }
#     return render(request, 'paginas/carrossel.html', context)