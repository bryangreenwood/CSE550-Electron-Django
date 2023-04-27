from django.db import models

# Create your models here.

class Sensor(models.Model):
    UTC_Datetime = models.DateTimeField()
    timezone_offset = models.IntegerField(default=0)
    Embrace_firmware_version = models.CharField(max_length=20)
    App = models.CharField(max_length=10)
    App_version = models.CharField(max_length=10)
    Mobile_OS = models.CharField(max_length=10)
    Mobile_OS_version = models.CharField(max_length=10)
    GTCS_algortithm_version = models.CharField(max_length=10)
    sensor_number = models.CharField(max_length=200, primary_key=True)
    
    class Meta:
        verbose_name_plural = "Sensors"
    
    def __str__(self):
        return self.sensor_number

class Sensordata(models.Model):
    sensor = models.ForeignKey(Sensor, default=None, verbose_name='Sensors', on_delete=models.CASCADE)
    UTC_Datetime = models.DateTimeField()
    timezone_offset = models.IntegerField(default=0)
    UNIX_timestamp = models.FloatField()
    Acc_magnitude_avg = models.FloatField()
    eda_avg = models.FloatField()
    Temp_avg = models.FloatField()
    movement_intensity = models.IntegerField()
    Steps = models.IntegerField()
    rest = models.IntegerField()
    on_wrist = models.BooleanField()

    class Meta:
        verbose_name_plural = "SesnorData"
        ordering = ['sensor_id', 'UTC_Datetime']
    def __str__(self):
        return self.sensor_id
    
# class subject(models.Model):
