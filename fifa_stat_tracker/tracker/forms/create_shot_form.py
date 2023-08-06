from django import forms
from tracker.models.player import Player


class CreateShotForm(forms.Form):
    
    def __init__(self, team, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player'].queryset = Player.objects.filter(team=team)
    
    minute = forms.IntegerField()
    corner = forms.BooleanField(required=False)
    on_target = forms.BooleanField(required=False)
    blocked_by_player = forms.BooleanField(required=False)
    body_part = forms.ChoiceField(choices=[('Foot', 'Foot'), ('Head', 'Head')])
    player = forms.ModelChoiceField(queryset=Player.objects.all())