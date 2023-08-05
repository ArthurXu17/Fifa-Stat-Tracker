from django.shortcuts import redirect
from django.views.generic import FormView

from tracker.forms.create_match_form import CreateMatchForm
from tracker.models.match import Match


class StartGameView(FormView):
    form_class = CreateMatchForm
    template_name = 'tracker/start_game.html'
    
    def form_valid(self, form):
        opponent = form.cleaned_data['opponent']
        round = form.cleaned_data['round']
        home_team = form.cleaned_data['home_team']
        match = Match.objects.create(opponent=opponent, round=round, home_team=home_team)
        return redirect(f'play_game/{match.id}')