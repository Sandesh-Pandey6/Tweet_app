from django.urls import path
from . import views 




urlpatterns = [
    path('', views.index, name='list_tweet'),  # Changed from 'listtweet' to 'list_tweet'
    
]
   

"""path('', views.list_tweet, name='list_tweet'),  # Changed from 'listtweet' to 'list_tweet'
    path('create/', views.create_tweet, name='create_tweet'),  # Changed from 'tweet_create' to 'create_tweet'
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
]"""