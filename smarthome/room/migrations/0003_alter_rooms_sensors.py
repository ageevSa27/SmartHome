# Generated by Django 3.2.3 on 2021-05-27 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_alter_rooms_sensors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='sensors',
            field=models.ManyToManyField(blank=True, to='room.Sensors'),
        ),
    ]
