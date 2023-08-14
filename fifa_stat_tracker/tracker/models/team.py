from django.db import models
from tracker.utilities import mean, median

class Team(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name
    
    def num_wins(self):
        return self.matches.filter(result='W').count()
    
    def num_draws(self):
        return self.matches.filter(result='D').count()
    
    def num_losses(self):
        return self.matches.filter(result='L').count()
    
    def average_stat_by_result(self, stat, result=None):
        matches = self.matches.filter(result=result) if result else self.matches.all()
        stat_list = [getattr(match, stat)() for match in matches]
        return mean(stat_list), median(stat_list)