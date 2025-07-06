from django import forms 
from .models import Tweet

class TweetForm(form.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text','photo']
