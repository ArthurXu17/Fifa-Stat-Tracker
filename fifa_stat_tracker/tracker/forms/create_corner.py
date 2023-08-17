from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class CreateCornerForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('create_corner', 'Create Corner'))
        
    
    minute = forms.IntegerField()
