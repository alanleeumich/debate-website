from django.db import models
import random
import string
# Create your models here.

def generate_unique_code():
    length = 8
    while True:
        code = "".join(random.choices(string.ascii_lowercase, k = length))
        if Room.objects.filter(code = code).count() == 0:
            break
    return code

class Room(models.Model):
    code = models.CharField(max_length=8,default = "", unique=True)
    aff_open = models.BooleanField(default=True)
    neg_open = models.BooleanField(default=True)

    def __str__(self):
        return self.id

class Message(models.Model):
    body = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    affirmative = models.BooleanField()
    
    
    def __str__(self):
        return self.body