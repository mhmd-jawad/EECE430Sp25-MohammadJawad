from django import forms
from .models import VolleyPlayer


class VolleyPlayerForm(forms.ModelForm):
    class Meta:
        model = VolleyPlayer
        fields = ['name', 'date_joined', 'position', 'salary', 'contact_person']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Player name'}),
            'date_joined': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact person name'}),
        }
