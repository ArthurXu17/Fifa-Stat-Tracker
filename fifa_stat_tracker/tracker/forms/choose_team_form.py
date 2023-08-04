from django import forms

from tracker.models import Team


class ChooseTeamForm(forms.Form):
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        empty_label="Choose a Team",
        widget=forms.Select({
            'class': 'select-dropdown'
        }))
