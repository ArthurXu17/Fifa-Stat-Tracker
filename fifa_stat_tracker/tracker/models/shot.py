from django.db import models

from .corner import Corner
from .match import Match
from .player import Player

class Shot(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='shots')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='shots')
    corner = models.ForeignKey(Corner, on_delete=models.CASCADE, related_name='shots', blank=True, null=True)
    on_target = models.BooleanField()
    blocked_by_player = models.BooleanField()
    body_part = models.CharField(max_length=10, choices=[('Foot', 'Foot'), ('Head', 'Head')])
    minute = models.IntegerField()
    