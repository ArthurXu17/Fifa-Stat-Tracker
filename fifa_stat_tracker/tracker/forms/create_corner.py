from django import forms


class CreateCornerForm(forms.Form):
    minute = forms.IntegerField()
