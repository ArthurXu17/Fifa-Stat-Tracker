from django.db import models
from .team import Team

class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    number = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.number})"