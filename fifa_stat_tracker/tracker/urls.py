from django.urls import path

from .views.view_stats_view import ViewStatsView
from .views.play_game_view import play_game_view
from .views.make_team_view import MakeTeamView
from .views.view_team_stats_view import ViewTeamStatsView
from .views.start_game_view import StartGameView

urlpatterns = [
    # ex: /make_team/
    path("make_team", MakeTeamView.as_view(), name="make_team"),
    path("play_game/<int:match_id>", play_game_view, name="play_game"),
    path("start_game", StartGameView.as_view(), name="start_game"),
    path("view_stats", ViewStatsView.as_view(), name="view_stats"),
    path("view_stats/team/<int:pk>", ViewTeamStatsView.as_view(), name="view_team_stats")
]