from django import forms

class Pages(forms.Form):
    pages = forms.IntegerField(min_value=1)