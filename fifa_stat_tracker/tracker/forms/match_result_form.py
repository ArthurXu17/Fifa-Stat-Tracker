from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class MatchResultForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('end_game', 'End Game'))
        
    result = forms.ChoiceField(choices=[
        ('W', 'Win'),
        ('D', 'Draw'),
        ('L', 'Loss')],
        widget=forms.RadioSelect())