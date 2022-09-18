from django.urls import path
from . import views

urlpatterns = [
    path('messages',views.getAllMessages, name = "messages"),
    path('rooms',views.getAllRooms, name = "rooms"),
    path('join',views.test,name = "test")
]