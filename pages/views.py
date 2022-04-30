from django.views.generic import TemplateView

# Create your views here.


class index(TemplateView):
    template_name = 'pages/index.html'
