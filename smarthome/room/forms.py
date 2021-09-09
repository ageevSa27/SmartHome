from django import forms
from .models import *


class AddRoom(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'


class AddSensor(forms.ModelForm):
    class Meta:
        model = Sensors
        fields = '__all__'


class Addsensortoroom(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['sensors']


