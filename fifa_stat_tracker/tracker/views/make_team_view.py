from django.shortcuts import get_object_or_404, render, redirect

from tracker.models.team import Team
from tracker.models.player import Player
from tracker.forms.create_player_form import CreatePlayerForm
    
def make_team_view(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    create_player_form = CreatePlayerForm()
    if request.method == 'POST': 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        number = request.POST['number']
        position = request.POST['position']
        Player.objects.create(first_name=first_name, last_name=last_name, number=number, team=team, position=position)
        return redirect(f"/tracker/make_team/{team_id}")
    else:
        context = {"team": team,
                   "players": team.players.all(),
                   "create_player_form": create_player_form}
        return render(request, "tracker/make_team.html", context=context)