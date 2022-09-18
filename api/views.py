from pyexpat.errors import messages
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Message, Room, generate_unique_code
from .serializers import MessageSerializer, RoomSerializer


# Create your views here.
@api_view(['GET'])
def getAllMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many = True)
    return Response(serializer.data)



@api_view(['GET','PUT'])
def test(request):
    side = request.data["side"]
    if side == "aff":
        open_rooms = Room.objects.filter(aff_open = True)
        if open_rooms.count() == 0:
            code = generate_unique_code()
            room = Room(code = code, aff_open = False, neg_open = True)
            room.save()
            return Response(code)
        else:
            room = open_rooms.first()
            room.aff_open = False
            room.save()
            return Response(room.code)
    else:
        open_rooms = Room.objects.filter(neg_open = True)
        if open_rooms.count() == 0:
            code = generate_unique_code()
            room = Room(code = code, aff_open = True, neg_open = False)
            room.save()
            return Response(code)
        else:
            room = open_rooms.first()
            room.neg_open = False
            room.save()
            return Response(room.code)

    