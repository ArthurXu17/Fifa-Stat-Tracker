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
        header_prefix = "Header" if self.body_part == "Head" else ""
        goal = "GOOOAL" if self.is_impressive_goal else "Goal"
        goal += f" by {self.player.first_name} {self.player.last_name}"
        corner_suffix = f"generated from corner at {self.corner.minute}'" if self.corner is not None else ""
        if self.assist:
            assist = "assisted" if self.is_impressive_assist else "uhssisted"
            goal = f"{header_prefix} {goal} {assist} by {self.assist.first_name} {self.assist.last_name}"
        else:
            goal = f"Unassisted {header_prefix} {goal}"
        return f"{goal} at {self.minute}' {corner_suffix}"
    
    class Meta:
        default_related_name = 'goals'