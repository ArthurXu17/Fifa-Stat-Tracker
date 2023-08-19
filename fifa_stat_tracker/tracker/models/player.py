from django.db import models
from .team import Team

class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    number = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.number})"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def num_shots(self):
        return self.shots.count() + self.goals.count()
    
    def num_blocked_shots(self):
        return self.shots.filter(blocked_by_player=True).count()
    
    def num_shots_on_target(self):
        return self.shots.filter(on_target=True).count() + self.goals.count()
    
    def num_impressive_goals(self):
        return self.goals.filter(is_impressive_goal=True).count()
    
    def num_not_impressive_goals(self):
        return self.goals.filter(is_impressive_goal=False).count()
    
    def num_goals(self):
        return self.num_impressive_goals() + self.num_not_impressive_goals()
    
    def num_impressive_assists(self):
        return self.goals_assisted_on.filter(is_impressive_assist=True).count()
   
    def num_not_impressive_assists(self):
        return self.goals_assisted_on.filter(is_impressive_assist=False).count()
    
    def num_assists(self):
        return self.num_impressive_assists() + self.num_not_impressive_assists()
    
    def num_matches(self):
        return self.team.matches.count()
    
    def num_shots_per_ten(self):
        return self.num_shots() * 10 / self.num_matches()
    
    def num_shots_on_target_per_ten(self):
        return self.num_shots_on_target() * 10 / self.num_matches()
    
    def num_goals_per_ten(self):
        return  self.num_goals() * 10 / self.num_matches()
    
    def num_assists_per_ten(self):
        return self.num_assists() * 10 / self.num_matches()
    
    def goals_per_shot_on_target_percent(self):
        return self.num_goals() * 100 / self.num_shots_on_target()
    
    def shots_on_target_per_shot_percent(self):
        return self.num_shots_on_target() * 100 / self.num_shots()