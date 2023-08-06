from django.db import models

from .corner import Corner
from .match import Match
from .player import Player

class AbstractShot(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    corner = models.ForeignKey(Corner, on_delete=models.CASCADE, blank=True, null=True)
    on_target = models.BooleanField()
    blocked_by_player = models.BooleanField()
    body_part = models.CharField(max_length=10, choices=[('Foot', 'Foot'), ('Head', 'Head')])
    minute = models.IntegerField()
    
    class Meta:
        abstract = True