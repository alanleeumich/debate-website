from rest_framework.serializers import ModelSerializer
from .models import Message, Room, Community,Prompt
from django.contrib.auth.models import User

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','body','created','affirmative']

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id','aff_open','neg_open','code']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'id']

class CommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['id','name','admins','prompts','currentPrompt']

class PromptSerializer(ModelSerializer):
    class Meta:
        model = Prompt
        fields = ['id','body']