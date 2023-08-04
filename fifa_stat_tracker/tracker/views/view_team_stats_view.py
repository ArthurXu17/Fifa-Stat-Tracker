from django.views.generic import DetailView

from tracker.models.team import Team


class ViewTeamStatsView(DetailView):
    model = Team
    template_name = 'tracker/view_team_stats.html'