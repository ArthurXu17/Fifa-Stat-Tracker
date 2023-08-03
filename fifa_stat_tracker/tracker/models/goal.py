from django.db import models

from .shot import Shot
from .player import Player

class Goal(Shot):
    assist = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goals_assisted_on', blank=True, null=True)
    is_impressive_assist = models.BooleanField(blank=True, null=True)
    is_impressive_goal = models.BooleanField()