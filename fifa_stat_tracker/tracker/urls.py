from django.urls import path

from .views.view_stats_view import ViewStatsView
from .views.play_game_view import PlayGameView
from .views.make_team_view import MakeTeamView
from .views.view_team_stats_view import ViewTeamStatsView

urlpatterns = [
    # ex: /make_team/
    path("make_team", MakeTeamView.as_view(), name="make_team"),
    path("play_game", PlayGameView.as_view(), name="play_game"),
    path("view_stats", ViewStatsView.as_view(), name="view_stats"),
    path("view_stats/team/<int:pk>", ViewTeamStatsView.as_view(), name="view_team_stats")
]