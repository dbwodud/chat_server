from django import forms
from .models import Room
class roomForm(forms.Form):
    room_name = forms.CharField(label="채팅방 제목")

