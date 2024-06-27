from .models import SongModel,SongGenre
from rest_framework import serializers

class SongSerializers(serializers.ModelSerializer):
    genre_name = serializers.CharField(source='genre.song_genre', read_only=True)
    author_nickname = serializers.CharField(source='author_nickname.nickname', read_only=True)

    class Meta:
        model = SongModel
        fields = ['id', 'slug', 'song_name', 'description', 'song_text', 'song_image', 'song', 'author', 'genre_name','author_nickname']

    def create(self, validated_data):
        validated_data['author']=self.context['request'].user
        post=super().create(validated_data)
        post.save()
        return post
    


class SongGengreSerializer(serializers.ModelSerializer):
    class Meta:
        model=SongGenre
        fields='__all__'