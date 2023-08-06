from django.db import models

from .abstract_shot import AbstractShot
from .player import Player

class Goal(AbstractShot):
    
    on_target = True
    blocked_by_player = False
    assist = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='goals_assisted_on', blank=True, null=True)
    is_impressive_assist = models.BooleanField(blank=True, null=True)
    is_impressive_goal = models.BooleanField()
    
    def display_information(self):
        return f"Goal by {self.player.first_name} {self.player.last_name} at {self.minute}'"
    
    class Meta:
        default_related_name = 'goals'