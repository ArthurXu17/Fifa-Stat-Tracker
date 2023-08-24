from django.forms import ModelForm
from tracker.models.player import Player
from crispy_forms.layout import Layout, Row, Column, Submit
from crispy_forms.helper import FormHelper

class CreatePlayerForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('add_player', 'Add Player'))
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='col-2'),
                Column('last_name', css_class='col-2'),
                Column('number', css_class='col-2'),
                Column('position', css_class='col-2'),
                Column('overall', css_class='col-2'),
            )
        )
            
    class Meta:
        model = Player
        fields = ["first_name", "last_name", "number", "position", "overall"]