from django.db import models
from .match import Match

class Corner(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='corners')