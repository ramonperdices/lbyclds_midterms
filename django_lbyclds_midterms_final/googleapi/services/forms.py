from django import forms

class MyForm(forms.Form):
    longitude = forms.IntegerField()
    latitude = forms.IntegerField()
