from django.views.generic import TemplateView


class PlayGameView(TemplateView):
    template_name = 'tracker/play_game.html'