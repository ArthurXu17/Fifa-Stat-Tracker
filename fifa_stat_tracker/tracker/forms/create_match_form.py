from django.forms import ModelForm
from tracker.models.match import Match

class CreateMatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ["opponent", "round", "home_team"]