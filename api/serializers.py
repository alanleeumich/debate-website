from rest_framework.serializers import ModelSerializer
from .models import Message
from .models import Room

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','body','created','affirmative']

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','aff_open','neg_open','code']