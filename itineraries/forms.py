from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from datetime import date
from .models import Itinerary

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ["destination", "start", "end"]
        
    destination = forms.CharField(widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'data-target' : '#'
        }))
    start = forms.DateField(widget=forms.DateInput(attrs={
            'class': 'form-control datepicker-input',
            'data-target': '#datepicker1'
        }))
    
    end = forms.DateField(widget=forms.DateInput(attrs={
            'class': 'form-control datepicker-input',
            'data-target': '#datepicker1'
        }))

class FindPlaces(forms.Form):
    types = ((1, "restaurants"), (2, "attractions"), (3, "parks"), 
            (4, "national parks"), (5, "clothing stores"), (6, "malls"), 
            (7, "department stores"), (8, "stadiums"))

    place_type = forms.ChoiceField(choices=types)

