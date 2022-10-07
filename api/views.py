from pyexpat.errors import messages
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework import views
from .models import Message, Room, Community, Prompt, generate_unique_code
from .serializers import *
import json

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

@api_view(['GET'])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllCommunities(request):
    communities = Community.objects.all()
    serializer = CommunitySerializer(communities,many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllPrompts(request):
    prompts = Prompt.objects.all()
    serializer = PromptSerializer(prompts, many = True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
def createUser(request):
    if User.objects.filter(username = request.data['username']).count() == 0:
        user = User.objects.create_user(request.data['username'],email = request.data['email'], password = request.data['password'])
        print(request.data['email'], request.data['password'])

        user.save()
        return Response("success")
    return Response("user already exists")        

class LoginView(views.APIView):
    def post(self,request):
        body = json.loads(request.body.decode('utf-8'))

        
        user = authenticate(username = body["username"], password = body["password"])
        if user == None:
            return Response("failed login")
        
        login(request,user)
        return Response("successful login")


@api_view(['GET','POST'])
def makeCommunity(request):
    username = request.data["auth"]["username"]
    password = request.data["auth"]["password"]
    user = authenticate(username = username, password = password)
    if user == None:
        return Response("error, invalid user")
    
    community_name = request.data["community"]["name"]
    
    if Community.objects.filter(name = community_name).count() != 0:
        return Response("error, community name already taken")

    community = Community(name = community_name)
    community.save()
    community.admins.add(user)
    for prompt_body in request.data["community"]["prompts"]:
        prompt = Prompt(body = prompt_body,community = community)
        prompt.save()
    return Response("created community successfully")

@api_view(['GET,POST'])
def addPrompt(request):
    username = request.data["auth"]["username"]
    password = request.data["auth"]["password"]
    user = authenticate(username = username, password = password)
    if user == None:
        return Response("error, invalid user")
    
    community_name = request.data["community"]
    if Community.objects.filter(name = community_name).count() == 0:
        return Response("no community with name exists")
    community = Community.objects.filter(name = community_name)[0]
    if not user in community.admins.all():
        return Response("user is not admin")
    
    prompt = Prompt(body = request.data["prompt"],community = community)
    prompt.save()
    return Response("prompt successfully added")

@api_view(['GET','POST'])
def deletePrompt(request):
    username = request.data["auth"]["username"]
    password = request.data["auth"]["password"]
    user = authenticate(username = username, password = password)
    if user == None:
        return Response("error, invalid user")
    prompt_id = request.data["promptId"]
    if Prompt.objects.filter(id = prompt_id).count() == 0:
        return Response("prompt id invalid")
    prompt = Prompt.objects.filter(id = prompt_id)[0]
    if not user in prompt.community.admins.all():
        return Response("user is not admin")
    prompt.delete()
    return Response("prompt deleted sucessfully")


@api_view(['GET','POST'])
def getUser(request):
    
    username = request.data["auth"]["username"]
    password = request.data["auth"]["password"]
    user = authenticate(username = username, password = password)
    if user == None:
        return Response("error, invalid user")
    
    retval = {}
    communities = user.communities.all()
    for community in communities:
        retval[community.name] = []
        for prompt in community.prompts.all():
            retval[community.name].append(prompt.body)
    return Response(json.dumps(retval))






@api_view(['GET','PUT'])
def getRoom(request):
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

    