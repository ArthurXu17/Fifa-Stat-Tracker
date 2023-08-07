from django.views.generic import DetailView

from tracker.models.team import Team


class MakeTeamView(DetailView):
    model = Team
    template_name = 'tracker/make_team.html'