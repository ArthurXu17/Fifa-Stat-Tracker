from django.db import models

from .abstract_shot import AbstractShot

class Shot(AbstractShot):
    
    def display_information(self):
        verb = "Shot" if self.body_part == "Foot" else "Header"
        on_target = "on target" if self.on_target else "off target"
        corner_suffix = f"generated from corner at {self.corner.minute}'" if self.corner is not None else ""
        blocked = "Blocked" if self.blocked_by_player else ""
        return f"{blocked} {verb} {on_target} by {self.player.first_name} {self.player.last_name} at {self.minute}' {corner_suffix}"
    
    class Meta:
        default_related_name = 'shots'