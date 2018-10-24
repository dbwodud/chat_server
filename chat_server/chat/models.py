from django.db import models

# Create your models here.


#chatting room db
class Room(models.Model):
    room_name = models.TextField()

class Chat(models.Model):
    room_name = models.ForeignKey(Room,on_delete=models.CASCADE)
    chat = models.TextField(null=True,blank=True)

