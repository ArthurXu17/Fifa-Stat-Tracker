from django.forms import ModelForm
from tracker.models.player import Player

class CreatePlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ["first_name", "last_name", "number", "position"]