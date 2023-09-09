from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'tracker/home_page.html'