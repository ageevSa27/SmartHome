from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *


def home(request):
    return render(request, 'room/home.html')


def rooms(request, ):
    rooms = Rooms.objects.all()

    context = {
        "rooms": rooms,
        "sensors": sensors,
    }

    return render(request, 'room/rooms.html', context)


def sensors(request):
    sensors = Sensors.objects.all()
    return render(request, 'room/sensors.html', {'sensors': sensors})


def roominfo(request, room_id):
    room = Rooms.objects.filter(id=room_id)
    return render(request, 'room/roominfo.html', {'room': room})


def sensorinfo(request, sensor_id):
    sensor = Sensors.objects.filter(id=sensor_id)
    return render(request, 'room/sensorinfo.html', {'sensor': sensor})


def addroom(request):
    if request.method == "POST":
        add_room = AddRoom(request.POST)
        if add_room.is_valid():
            try:
                add_room.save()
                return redirect('rooms')
            except:
                add_room.add_error(None, 'Ошибка добавления комнаты')

    else:
        add_room = AddRoom()
    return render(request, 'room/addroom.html', {"form": add_room})


def addsensor(request):
    if request.method == "POST":
        add_sensor = AddSensor(request.POST)
        if add_sensor.is_valid():
            try:
                add_sensor.save()
                return redirect('sensors')
            except:
                add_sensor.add_error(None, 'Ошибка добавления датчика')
    else:
        add_sensor = AddSensor()
    return render(request, 'room/addsensor.html', {"form": add_sensor})


def deliteroom(request, room_id):
    room = Rooms.objects.filter(id=room_id)
    room.delete()
    return redirect(rooms)


def delitesensor(request, sensor_id):
    sensor = Sensors.objects.filter(id=sensor_id)
    sensor.delete()
    return redirect(sensors)


def sensortoroom(request, room_id):
    if request.method == "POST":
        form = Addsensortoroom(request.POST)
        if form.is_valid():
            sensor = request.POST.get("sensors")
            print(sensor)
            room = Rooms.objects.get(id=room_id)
            room.sensors.add(Sensors.objects.get(id=sensor))
            room.save()

    else:
        form = Addsensortoroom()
    return render(request, 'room/addsensortoroom.html', {'form': form, 'room_id': room_id})

