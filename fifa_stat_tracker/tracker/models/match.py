from django.db import models

class Match(models.Model):
    opponent = models.CharField(max_length=20)
    round = models.CharField(max_length=20, choices=[
        ('GR', 'Group Stage'),
        ('R16', 'Round of 16'),
        ('QF', 'Quarter Finals'),
        ('SF', 'Semi Finals'),
        ('F', 'Finals')
    ])