from django.db import models
from .match import Match

class Corner(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='corners')
    minute = models.IntegerField()
    
    def display_information(self):
        return f"Corner kick"
    
    def num_shots_generated(self):
        return self.shots.count()
    
    def num_goals_generated(self):
        return self.goals.count()