from django import forms
from django.forms import (formset_factory)

""" url form 
@param django form 
"""
class UrlForm(forms.Form):
    url = forms.CharField(
        label='Url',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Url here',
            'required': 'required'
        }),
        
    )

UrlFormset = formset_factory(UrlForm)
