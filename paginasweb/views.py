from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = "paginasweb/index.html"