from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#chatting room db
class Room(models.Model):
    room_name = models.TextField(null=True,blank=True)
    who_create = models.ForeignKey(User,on_delete=models.CASCADE,default='') 
    user_list = models.TextField(default='')
    user = models.TextField(default='')

    def __str__(self):
        return self.room_name

class Chat(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    chat = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.chat

