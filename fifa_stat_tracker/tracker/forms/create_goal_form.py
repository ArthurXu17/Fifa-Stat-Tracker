from django import forms
from tracker.utilities import BODY_PART_OPTIONS
from tracker.models.player import Player
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit


class CreateGoalForm(forms.Form):
    
    def __init__(self, team, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player'].queryset = Player.objects.filter(team=team)
        self.fields['assist'].queryset = Player.objects.filter(team=team)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('minute', css_class='col-3'),
                Column('body_part', css_class='col-3'),
                Column('player', css_class='col-3'),
                Column('assist', css_class='col-3')
            ),
            Row(
                Column('corner', css_class='col-3'),
                Column(css_class='col-3'),
                Column('impressive_goal', css_class='col-3'),
                Column('impressive_assist', css_class='col-3')
            )
        )
        self.helper.add_input(Submit('create_goal', 'Create Goal'))

    minute = forms.IntegerField()
    body_part = forms.ChoiceField(choices=BODY_PART_OPTIONS)
    corner = forms.BooleanField(required=False, label='Generated by Last Corner')
    impressive_goal = forms.BooleanField(required=False)
    impressive_assist = forms.BooleanField(required=False)
    player = forms.ModelChoiceField(queryset=Player.objects.all())
    assist = forms.ModelChoiceField(queryset=Player.objects.all(), required=False)
    