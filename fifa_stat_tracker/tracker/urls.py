from django.urls import path

from .views.home_page_view import HomePageView
from .views.view_stats_view import ViewStatsView
from .views.play_game_view import play_game_view
from .views.initialize_team_view import InitializeTeamView
from .views.view_team_stats_view import ViewTeamStatsView
from .views.start_game_view import StartGameView
from .views.make_team_view import make_team_view
from .views.top_players_view import TopPlayersView
from .views.user_stats_view import UserStatsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home_page"),
    path("initialize_team", InitializeTeamView.as_view(), name="initialize_team"),
    path("play_game/<int:match_id>", play_game_view, name="play_game"),
    path("start_game", StartGameView.as_view(), name="start_game"),
    path("view_stats", ViewStatsView.as_view(), name="view_stats"),
    path("view_stats/team/<int:pk>", ViewTeamStatsView.as_view(), name="view_team_stats"),
    path("make_team/<int:team_id>", make_team_view, name="make_team"),
    path("top_players", TopPlayersView.as_view(), name="top_players"),
    path("user_stats", UserStatsView.as_view(), name="user_stats")
]