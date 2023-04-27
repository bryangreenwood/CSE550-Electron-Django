from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from main.models import Sensor, Sensordata
from Group5.utils import eval_bool
def upload_file(request):
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index==0:
                    pass
                else:
                    print(obj.file_name)
                    if "metadata" in  str(obj.file_name):
                    
                        Sensor.objects.create(
                            UTC_Datetime = row[0], 
                            timezone_offset = row[1],
                            Embrace_firmware_version = row[2],
                            App = row[3],
                            App_version = row[4],
                            Mobile_OS = row[5],
                            Mobile_OS_version = row[6],
                            GTCS_algortithm_version = row[7],
                            sensor_number = row[8]
                        )   
                        obj.activated = True


                    elif "summary" in str(obj.file_name):

                        Sensordata.objects.create(
                                UTC_Datetime = row[0],
                                timezone_offset = row[1],
                                UNIX_timestamp = row[2],
                                Acc_magnitude_avg = row[3],
                                eda_avg = row[4],
                                Temp_avg = row[5],
                                movement_intensity = row[6],
                                Steps = row[7],
                                rest = row[8],
                                on_wrist = eval_bool(row[9]),
                                sensor = Sensor.objects.get(sensor_number=row[10])
                        )
                    else:
                        obj.delete()
                        raise Exception("This is not a valid format for a file, please upload either a metadata or summary file.")
                obj.activated = True
                obj.save()
    else:
        print(form.errors)

                
    return render(request, 'csvs/upload.html',{'form':form, 'title':'Upload'})
