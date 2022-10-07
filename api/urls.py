from django.urls import path
from . import views

urlpatterns = [
    path('messages',views.getAllMessages, name = "messages"),
    path('rooms',views.getAllRooms, name = "rooms"),
    path('communities',views.getAllCommunities,name = "communities"),
    path('users',views.getAllUsers, name = "users"),
    path('prompts',views.getAllPrompts, name = "prompts"),
    
    
    path('join',views.getRoom,name = "test"),
    
    
    path('create-user',views.createUser,name = "create-user"),
    path('login',views.LoginView.as_view(),name = "login"),
    path('get-user',views.getUser,name = "getUser"),
    path('make-community',views.makeCommunity, name = "makeCommunity")

]