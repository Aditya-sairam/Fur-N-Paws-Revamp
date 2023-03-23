from django import forms
from .models import DogWalkerDetails

class DogWalkerDetailsForm(forms.ModelForm):
    class Meta:
        model = DogWalkerDetails
        fields = ['image', 'Age', 'Profession', 'Availability', 'adress', 'mobile_no']

