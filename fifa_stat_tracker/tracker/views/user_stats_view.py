import functools
from django.views.generic import TemplateView

from tracker.models.corner import Corner
from tracker.models.match import Match
from tracker.models.goal import Goal
from tracker.utilities import Record, make_comparator, compareRecords, ROUND_OPTIONS, POSITION_OPTIONS


class UserStatsView(TemplateView):
    template_name = 'tracker/user_stats.html'
    
    def get_records_vs_teams(self):
        record_list = []
        opponent_names = Match.objects.values_list('opponent').distinct()
        for opponent in opponent_names:
            wins = Match.objects.filter(opponent=opponent[0], result='W').count()
            draws = Match.objects.filter(opponent=opponent[0], result='D').count()
            losses = Match.objects.filter(opponent=opponent[0], result='L').count()
            record_list.append(Record(wins, draws, losses, opponent[0]))
        
        key_function = functools.cmp_to_key(make_comparator(compareRecords))
        return sorted(record_list, key=key_function, reverse=True)
    
    def corner_stats(self):
        corners = Corner.objects.all()
        total = corners.count()
        no_shots = [corner for corner in corners if corner.num_goals_generated() == 0 and corner.num_shots_generated() == 0]
        goal_corners = [corner for corner in corners if corner.num_goals_generated() > 0]
        one_shot_corners = [corner for corner in corners if corner.num_goals_generated() == 0 and corner.num_shots_generated() == 1]
        multi_shot_corners = [corner for corner in corners if corner.num_goals_generated() == 0 and corner.num_shots_generated() > 1]
        return {'num_no_shot_corners': len(no_shots),
                'num_one_shot_corners': len(one_shot_corners),
                'num_multi_shot_corners': len(multi_shot_corners),
                'num_goal_corners': len(goal_corners),
                'total': total}
    
    def get_records_by_rounds(self):
        record_list = []
        for round, description in ROUND_OPTIONS:
            wins = Match.objects.filter(round=round, result='W').count()
            draws = Match.objects.filter(round=round, result='D').count()
            losses = Match.objects.filter(round=round, result='L').count()
            record_list.append(Record(wins, draws, losses, description))
        return record_list
    
    def get_assist_patterns(self):
        positions = [pos[0] for pos in POSITION_OPTIONS]
        all_patterns = []
        for p1 in positions:
            for p2 in positions:
                if p1 != p2:
                    all_patterns.append((p1,p2))
        
        pattern_counts = []
        for assist, scorer in all_patterns:
            num_occurences = Goal.objects.filter(assist__position=assist,
                                                 player__position=scorer,
                                                 corner__isnull=True).count()
            pattern_counts.append((f"{assist} to {scorer}", num_occurences))
        
        sorted_list = sorted(pattern_counts, key=lambda pair: pair[1], reverse=True)
        result = sorted_list[:8]
        other_count = 0
        for _, num in sorted_list[8:]:
            other_count +=  num
        result.append(("Other", other_count))
        num_unassisted = Goal.objects.filter(assist__isnull=True,
                                             corner__isnull=True).count()
        result.append(("Unassisted", num_unassisted))
        return result
    
    def get_context_data(self, **kwargs):
        records_by_opponents = self.get_records_vs_teams()
        context = super().get_context_data(**kwargs)
        corner_stats = self.corner_stats()
        records_by_rounds = self.get_records_by_rounds()
        assist_patterns = self.get_assist_patterns()
        context.update({
            'records_by_opponents': records_by_opponents,
            'corner_stats': corner_stats,
            'records_by_rounds': records_by_rounds,
            'assist_patterns': assist_patterns
        })
        return context