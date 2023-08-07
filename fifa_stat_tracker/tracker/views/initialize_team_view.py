from django.shortcuts import redirect
from django.views.generic import FormView
from tracker.forms.initialize_team_form import InitializeTeamForm
from tracker.models.team import Team


class InitializeTeamView(FormView):
    form_class = InitializeTeamForm
    template_name = 'tracker/initialize_team.html'
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        team = Team.objects.create(name=name)
        return redirect(f'make_team/{team.id}')