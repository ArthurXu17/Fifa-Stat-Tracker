from django.shortcuts import redirect
from django.views.generic import FormView

from tracker.forms.choose_team_form import ChooseTeamForm


class ViewStatsView(FormView):
    form_class = ChooseTeamForm
    template_name = 'tracker/view_stats.html'
    
    def form_valid(self, form):
        team = form.cleaned_data['team']
        return redirect(f'view_stats/team/{team.id}')