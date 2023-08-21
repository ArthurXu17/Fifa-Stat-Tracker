from django.views.generic import TemplateView

from tracker.models.player import Player

class TopPlayersView(TemplateView):
    template_name = 'tracker/top_players.html'
    
    def best_players_by_stat(self, stat, precondition=lambda player:True):
        """
        Args:
            stat (string): stats to find best players by
            precondition (function: Player -> Bool, optional): Precondition on which players to consider. Defaults to function that returns True for all players
        """
        all_players = [p for p in Player.objects.all() if precondition(p)]
        sorted_players = sorted(all_players, key=lambda player: getattr(player, stat)(), reverse=True)
        top_players =  sorted_players[:10]
        return [{'player': p,
                 'name': p.full_name(),
                 'team': p.team.name,
                 'position': p.position,
                 stat: f'{getattr(p, stat)():.2f}'} for p in top_players]
    
    def get_context_data(self, **kwargs):
        # shots
        shot_players = self.best_players_by_stat('num_shots_per_ten')
        # shots on target
        shot_on_target_players = self.best_players_by_stat('num_shots_on_target_per_ten')
        # goals
        goal_players = self.best_players_by_stat('num_goals_per_ten')
        # assists
        assist_players = self.best_players_by_stat('num_assists_per_ten')
        # shot_on_target_percentage
        shot_on_target_percent_players = self.best_players_by_stat('shots_on_target_per_shot_percent',
                                                                   lambda player: player.num_shots() >= 10)
        for info in shot_on_target_percent_players:
            info['shots'] = info['player'].num_shots()
            info['shots_on_target'] = info['player'].num_shots_on_target()
        # goal percentage
        goal_percent_players = self.best_players_by_stat('goals_per_shot_on_target_percent',
                                                         lambda player: player.num_shots_on_target() >= 5)
        for info in goal_percent_players:
            info['goals'] = info['player'].num_goals()
            info['shots_on_target'] = info['player'].num_shots_on_target()
        context = super().get_context_data(**kwargs)
        context.update({
            'shot_players': shot_players,
            'shot_on_target_players': shot_on_target_players,
            'goal_players': goal_players,
            'assist_players': assist_players,
            'shot_on_target_percent_players': shot_on_target_percent_players,
            'goal_percent_players': goal_percent_players,
        })
        return context