from .models import UserCabinet
from rest_framework.serializers import ModelSerializer

class UserCabinetSerializer(ModelSerializer):
    class Meta:
        model=UserCabinet
        fields='__all__'

    
    def create(self, validated_data):
        validated_data['author']=self.context['request'].user
        post=super().create(validated_data)
        post.save()
        return post