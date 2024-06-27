from rest_framework import serializers
from songs.serializers import SongSerializers
from .models import Playlist

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['songs'] = SongSerializers(instance.songs.all(), many=True).data
        return representation

