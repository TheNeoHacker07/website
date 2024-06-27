from django.contrib import admin
from .models import SongModel,SongGenre

admin.site.register(SongModel)
admin.site.register(SongGenre)

# Register your models here.
