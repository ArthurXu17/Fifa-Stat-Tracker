from django.db import models
from .team import Team

class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    number = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.number})"
    
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
    
    def num_impressive_assists(self):
        return self.goals_assisted_on.filter(is_impressive_assist=True).count()
   
    def num_not_impressive_assists(self):
        return self.goals_assisted_on.filter(is_impressive_assist=False).count()