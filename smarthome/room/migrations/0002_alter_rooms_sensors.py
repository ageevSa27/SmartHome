# Generated by Django 3.2.3 on 2021-05-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='sensors',
            field=models.ManyToManyField(blank=True, related_name='sensor', to='room.Sensors'),
        ),
    ]
