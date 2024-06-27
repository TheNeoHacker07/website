from django.db import models
from django.contrib.auth import get_user_model
from songs.models import SongGenre 
from django.utils.text import slugify
# Create your models here.

User=get_user_model()

class UserCabinet(models.Model):
    author=models.OneToOneField(User,related_name='user_cabinet',on_delete=models.CASCADE,verbose_name='пользаватель', blank=True)
    nickname=models.CharField(max_length=100,verbose_name='имя')
    slug=models.SlugField(max_length=50,unique=True,blank=False)
    about_user=models.CharField(max_length=123,verbose_name='О себе')
    favorite_genres=models.ForeignKey('songs.SongGenre',on_delete=models.SET_NULL,null=True,verbose_name='любимый жанр',blank=True)
    user_image=models.ImageField(upload_to='user/img/',verbose_name='фото пользавателя',blank=True)
    image=models.ImageField(upload_to='banner/img/',verbose_name='фото баннера',blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.nickname)
        super().save(*args,**kwargs)





    def __str__(self) -> str:
        return self.nickname




