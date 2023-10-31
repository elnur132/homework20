from django import forms
from django.forms import ModelForm
from .models import People

class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ('name','date_of_birth')
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control form-control-lg form-control-solid"}),
            'date_of_birth': forms.DateInput(format=('%Y-%m-%d'),
        attrs={'class': 'form-control', 
            'placeholder': 'Select a date',
            'type': 'date'
            }),
        }