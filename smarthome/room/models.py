from django.db import models

# Create your models here.
from django.urls import reverse


class Sensors(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sensorinfo', kwargs={'sensor_id': self.pk})

    def dell(self):
        return reverse('delitesensor', kwargs={'sensor_id': self.pk})



class Rooms(models.Model):
    name = models.CharField(max_length=150, blank=False)
    x = models.SmallIntegerField()
    y = models.SmallIntegerField()
    h = models.SmallIntegerField()
    sensors = models.ManyToManyField(Sensors, blank=True)

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('roominfo', kwargs={'room_id': self.pk})

    def dell(self):
        return reverse('deliteroom', kwargs={'room_id': self.pk})
    def addsens(self):
        return  reverse('sensortoroom', kwargs={'room_id': self.pk})