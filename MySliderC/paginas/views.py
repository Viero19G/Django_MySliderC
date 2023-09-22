from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "paginas/index.html"

class GradeView(TemplateView):
    template_name = "paginas/grade.html"