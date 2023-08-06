from django.db import models

from .abstract_shot import AbstractShot

class Shot(AbstractShot):
    
    def display_information(self):
        return f"Shot by {self.player.first_name} {self.player.last_name} at {self.minute}'"
    
    class Meta:
        default_related_name = 'shots'