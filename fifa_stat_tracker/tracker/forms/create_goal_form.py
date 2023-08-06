from django import forms
from tracker.models.player import Player


class CreateGoalForm(forms.Form):
    
    def __init__(self, team, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player'].queryset = Player.objects.filter(team=team)
        self.fields['assist'].queryset = Player.objects.filter(team=team)
    
    minute = forms.IntegerField()
    body_part = forms.ChoiceField(choices=[('Foot', 'Foot'), ('Head', 'Head')])
    corner = forms.BooleanField(required=False)
    impressive_goal = forms.BooleanField(required=False)
    impressive_assist = forms.BooleanField(required=False)
    player = forms.ModelChoiceField(queryset=Player.objects.all())
    assist = forms.ModelChoiceField(queryset=Player.objects.all(), required=False)
    