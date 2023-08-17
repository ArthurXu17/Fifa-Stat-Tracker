from django.db import models
from .team import Team

class Match(models.Model):
    opponent = models.CharField(max_length=20)
    round = models.CharField(max_length=20, choices=[
        ('GR', 'Group Stage'),
        ('R16', 'Round of 16'),
        ('QF', 'Quarter Finals'),
        ('SF', 'Semi Finals'),
        ('F', 'Finals')
    ])
    result = models.CharField(max_length=15, choices=[
        ('W', 'Win'),
        ('D', 'Draw'),
        ('L', 'Loss'),
        ('IP', 'In Progress')], default='IP')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches')
    
    def __str__(self) -> str:
        return f"{self.round}: {self.home_team.name} vs {self.opponent}"
    
    def get_events_sorted(self):
        shots = list(self.shots.all())
        goals = list(self.goals.all())
        corners = list(self.corners.all())
        shots.extend(corners)
        shots.extend(goals)
        return sorted(shots, key=lambda event: event.minute)
    
    def get_latest_corner(self):
        return max(self.corners.all(), key=lambda corner: corner.minute)
    
    def num_shots(self):
        return self.shots.count() + self.goals.count()
    
    def num_blocked_shots(self):
        return self.shots.filter(blocked_by_player=True).count()
    
    def num_shots_on_target(self):
        return self.shots.filter(on_target=True).count() + self.goals.count()
    
    def num_goals(self):
        return self.goals.count()
    
    def num_assists(self):
        return self.goals.filter(assist__isnull=False).count()
    
    def num_corners(self):
        return self.corners.count()