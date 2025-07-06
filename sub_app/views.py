from django.shortcuts import render
from .models import Tweet
from .forms import TweetForms
from django.shortcuts import get_object_or_404, redirect



# Create your views here.
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at') 
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})


