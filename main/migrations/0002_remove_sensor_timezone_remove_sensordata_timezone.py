# Generated by Django 4.1 on 2023-04-26 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='timezone',
        ),
        migrations.RemoveField(
            model_name='sensordata',
            name='timezone',
        ),
    ]