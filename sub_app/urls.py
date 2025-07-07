from django.urls import path
from . import views 




urlpatterns = [
    path('', views.tweet_list, name='list_tweet'),  
    path('create/', views.tweet_create, name='create_tweet'),  
    path('<int:box_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:_id>/delete/', views.tweet_delete, name='tweet_delete'),
    
    
]