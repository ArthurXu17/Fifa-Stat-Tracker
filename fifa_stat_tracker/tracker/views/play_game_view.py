from django.views.generic import DetailView

from tracker.models.match import Match

class PlayGameView(DetailView):
    model = Match
    template_name = 'tracker/play_game.html'