from django.views.generic import DetailView

from tracker.models.team import Team


class ViewTeamStatsView(DetailView):
    model = Team
    template_name = 'tracker/view_team_stats.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = context['team']
        stats = [('num_shots', 'Shots'), ('num_blocked_shots', 'Blocked Shots'), ('num_shots_on_target', 'Shots on Target'), 
                 ('num_goals', 'Goals'), ('num_assists', 'Assists'), ('num_corners', 'Corners')]
        stat_rows = []
        for stat, formatted_stat in stats:
            win_mean = win_median = draw_mean = draw_median = loss_mean = loss_median = mean = median = "N/A"
            if team.matches.filter(result='W').exists():
                win_mean, win_median = team.average_stat_by_result(stat, result='W')
                win_mean = f"{win_mean:.2f}"
            if team.matches.filter(result='D').exists():
                draw_mean, draw_median = team.average_stat_by_result(stat, result='D')
                draw_mean = f"{draw_mean:.2f}"
            if team.matches.filter(result='L').exists():
                loss_mean, loss_median = team.average_stat_by_result(stat, result='L')
                loss_mean = f"{loss_mean:.2f}"
            if team.matches.count() > 0:
                mean, median = team.average_stat_by_result(stat)
                mean = f"{mean:.2f}"
            stat_rows.append({
                'stat': formatted_stat,
                'win_mean': win_mean,
                'win_median': win_median,
                'draw_mean': draw_mean,
                'draw_median': draw_median,
                'loss_mean': loss_mean,
                'loss_median': loss_median,
                'overall_mean': mean,
                'overall_median': median
            })
        context.update({'stat_rows': stat_rows})
        return context