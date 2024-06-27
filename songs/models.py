from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify



User=get_user_model()

class SongGenre(models.Model):
    song_genre=models.CharField(max_length=12,verbose_name='ЖАНР')
    slug=models.SlugField(max_length=30,unique=False,blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.song_genre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.song_genre



class SongModel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='songs')
    genre=models.ForeignKey(SongGenre,on_delete=models.SET_NULL,null=True,related_name='genre',blank=True)
    author_nickname=models.ForeignKey('cabinet.UserCabinet',on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(unique=False, max_length=35, blank=True)
    song_name=models.CharField(max_length=30,verbose_name='название',blank=True)
    description=models.CharField(max_length=100,verbose_name='описание')
    song_text=models.CharField(max_length=25000 ,verbose_name='текст песни')
    song_image=models.ImageField(upload_to='songs/image/',blank=True,verbose_name='картинка песни')
    song=models.FileField(upload_to='songs/audio/',blank=True)


        

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateField(auto_now=True)


    def __str__(self):
        return self.song_name
    










# Create your models here.

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.song_name)
        super().save(*args, **kwargs)
