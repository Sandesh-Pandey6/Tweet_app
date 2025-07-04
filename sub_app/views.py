from django.shortcuts import render
from .models import tweet 
from .forms import Tweet_form
from django.shortcuts import get_object_or_404 , redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')



def list_tweet(request):
    Tweet=tweet.objects.all().order_by('-created_at')
    return render (request, 'list_tweet.html',{'Tweet':Tweet})


def create_tweet(request):
    if request.method == "POST":
        form = Tweet_form(request.POST, request.FILES)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.user = request.user  
            new_tweet.save()
            return redirect('list_tweet')
            
    else:
        form = Tweet_form()

    return render(request, 'tweet_form.html', {'form': form})




def tweet_edit(request, tweet_id):
    tweet_obj = get_object_or_404(tweet, pk=tweet_id, user=request.user)  # Changed variable name
    if request.method == 'POST':
        form = Tweet_form(request.POST, request.FILES, instance=tweet_obj)
        if form.is_valid():
            form.save()
            return redirect('list_tweet')
    else:
        form = Tweet_form(instance=tweet_obj)
    return render(request, 'tweet_form.html', {'form': form})




def tweet_delete(request, tweet_id):
    new_tweet = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        new_tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'new_tweet':new_tweet})