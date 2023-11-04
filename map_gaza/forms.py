from django import forms
from .models import Map

class MapForm(forms.ModelForm):
    class Meta:
        model = Map
        fields = ['lat', 'lon', 'date', 'photo']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }