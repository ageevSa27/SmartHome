from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('rooms/', rooms, name='rooms'),
    path('sensors/', sensors, name='sensors'),
    path('addroom/', addroom, name='addroom'),
    path('addsensor/', addsensor, name='addsensor'),
    path('roominfo/<int:room_id>/', roominfo, name='roominfo'),
    path('deliteroom/<int:room_id>', deliteroom, name='deliteroom'),
    path('delitesensor/<int:sensor_id>', delitesensor, name='delitesensor'),
    path('sensorinfo/<int:sensor_id>/', sensorinfo, name='sensorinfo'),
    path('sensortoroom/<int:room_id>', sensortoroom, name='sensortoroom'),
]
