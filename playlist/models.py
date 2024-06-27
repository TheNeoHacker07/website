from django.db import models 
from django.contrib.auth import get_user_model
from songs.models import SongGenre

User = get_user_model()

class Playlist(models.Model):
    author = models.ForeignKey(User, related_name='playlist', on_delete=models.CASCADE, verbose_name='автор')
    name = models.CharField(max_length=25)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    songs = models.ManyToManyField(SongGenre, related_name='playlists')

    def __str__(self):
        return self.name

