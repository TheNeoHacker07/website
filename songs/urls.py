from django.urls import path
from .views import *


urlpatterns=[
    path('retrieve_song/<slug:slug>/',RetrieveSong.as_view()),
    path('list_song/',ListSong.as_view()),
    path('delete_song/<slug:slug>/',DeleteSong.as_view()),
    path('update_song/<slug:slug>/',UpdateSong.as_view()),
    path('post_song/',PostSong.as_view())
]