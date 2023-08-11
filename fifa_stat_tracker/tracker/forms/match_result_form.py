from django import forms

class MatchResultForm(forms.Form):
    result = forms.ChoiceField(choices=[
        ('W', 'Win'),
        ('D', 'Draw'),
        ('L', 'Loss')])