from django.db import models

# Create your models here.

#User

#chatting room db
class Room(models.Model):
    room_name = models.TextField()
    
    def __str__(self):
        return self.room_name

class Chat(models.Model):
    room_name = models.ForeignKey(Room,on_delete=models.CASCADE)
    chat = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.chat

