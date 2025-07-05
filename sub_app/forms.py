from django import forms 
from .models import tweet

class Tweet_form(forms.Form):
    class Meta:
        model = tweet
        fields = ('text', 'photo')  # fields you want to include in the form

    
