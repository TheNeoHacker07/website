from django.db import models
from django.contrib.auth import get_user_model
from songs.models import SongModel



User=get_user_model()


class Comment(models.Model):
    author=models.ForeignKey(User ,on_delete=models.CASCADE,related_name='comments')
    song=models.ForeignKey(SongModel,on_delete=models.CASCADE)
    
    body=models.TextField()
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)


class Like(models.Model):
    user=models.ForeignKey(User,related_name='likes',on_delete=models.CASCADE)
    song=models.ForeignKey(SongModel,related_name='likes',on_delete=models.CASCADE)














# Create your models here.
