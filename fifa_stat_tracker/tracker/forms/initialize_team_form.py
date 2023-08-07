from django.forms import ModelForm
from tracker.models.team import Team

class InitializeTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ["name"]