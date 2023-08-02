from django.views.generic import TemplateView


class MakeTeamView(TemplateView):
    template_name = 'tracker/make_team.html'