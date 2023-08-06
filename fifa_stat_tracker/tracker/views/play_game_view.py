from django.shortcuts import get_object_or_404, redirect, render
from tracker.models.match import Match
from tracker.models.corner import Corner
from tracker.models.shot import Shot
from tracker.models.goal import Goal
from tracker.forms.create_corner import CreateCornerForm
from tracker.forms.create_goal_form import CreateGoalForm
from tracker.forms.create_shot_form import CreateShotForm

def play_game_view(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    create_corner_form = CreateCornerForm()
    create_shot_form = CreateShotForm(team=match.home_team)
    create_goal_form = CreateGoalForm(team=match.home_team)
    if request.method == 'POST':
        print("post yeah")
        print(request.POST)
        if 'create_corner' in request.POST: 
            minute = request.POST['minute']
            Corner.objects.create(minute=minute, match=match)
        elif 'create_shot' in request.POST:
            minute = request.POST['minute']
            corner = match.get_latest_corner() if 'corner' in request.POST else None
            on_target = 'on_target' in request.POST
            blocked_by_player = 'blocked_by_player' in request.POST
            body_part = request.POST['body_part']
            player = int(request.POST['player'])
            Shot.objects.create(minute=minute, match=match, player_id=player, corner=corner,
                                on_target=on_target, blocked_by_player=blocked_by_player, body_part=body_part)
        elif 'create_goal' in request.POST:
            minute = request.POST['minute']
            corner = match.get_latest_corner() if 'corner' in request.POST else None
            assist = int(request.POST['assist']) if request.POST['assist'] != '' else None
            impressive_assist = 'impressive_assist' in request.POST if assist else None
            impressive_goal = 'impressive_goal' in request.POST
            body_part = request.POST['body_part']
            player = int(request.POST['player'])
            Goal.objects.create(minute=minute, match=match, player_id=player, corner=corner, body_part=body_part,
                                is_impressive_assist=impressive_assist, is_impressive_goal=impressive_goal, assist_id=assist)
        return redirect(f"/tracker/play_game/{match_id}")
    else: 
        context = {
            'match': match,
            'events': [event.display_information() for event in match.get_events_sorted()],
            'create_corner_form': create_corner_form,
            'create_shot_form': create_shot_form,
            'create_goal_form': create_goal_form
        }
        return render(request, "tracker/play_game.html", context=context)