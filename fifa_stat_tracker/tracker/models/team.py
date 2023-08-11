from django.db import models

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